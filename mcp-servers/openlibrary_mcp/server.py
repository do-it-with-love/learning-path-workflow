#!/usr/bin/env python3
"""Open Library MCP server — book lookup for the learning-path workflow.

A custom MCP server over Open Library's public API. No API key exists for it and
none is needed, which is why it was chosen: the workflow can be run from a clean
checkout with no credentials at all.

Its purpose in the workflow is narrow and important. The reading-curator must not
recommend books from model memory, and a book is exactly the kind of thing a model
will invent convincingly — plausible title, plausible author, wrong or nonexistent.
Every tool here returns a real Open Library record with a real URL, formatted so it
drops straight into the citation format the resource-vetting skill requires.

Only urllib is used for HTTP so the server has one dependency (the MCP SDK itself).

Docs: https://openlibrary.org/dev/docs/restful_api
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

from mcp.server.fastmcp import FastMCP

API = "https://openlibrary.org"
TIMEOUT = 20

# Open Library asks consumers to identify themselves; requests with a generic or
# missing User-Agent may be throttled or blocked outright.
USER_AGENT = os.environ.get(
    "OPENLIBRARY_USER_AGENT",
    "learning-path-workflow/1.0 (+https://github.com/; educational use)",
)

SEARCH_FIELDS = ",".join([
    "key", "title", "author_name", "first_publish_year", "number_of_pages_median",
    "isbn", "subject", "ebook_access", "language", "ratings_average", "ratings_count",
])

mcp = FastMCP("openlibrary")


def _get(path: str, params: dict[str, str | int]) -> dict:
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return {"__error__": f"Open Library returned HTTP {exc.code} for {url}"}
    except (urllib.error.URLError, TimeoutError) as exc:
        return {"__error__": f"could not reach Open Library ({exc}). Do not invent a "
                             f"substitute — report the failure instead."}
    except json.JSONDecodeError:
        return {"__error__": "Open Library returned a non-JSON response"}


def _format(doc: dict) -> str:
    """One record, in the workflow's citation shape."""
    key = doc.get("key", "")
    url = f"{API}{key}" if key.startswith("/") else API
    authors = ", ".join(doc.get("author_name") or []) or "unknown author"
    year = doc.get("first_publish_year") or "unknown"
    pages = doc.get("number_of_pages_median")
    isbns = doc.get("isbn") or []
    access = doc.get("ebook_access", "unknown")
    languages = ", ".join(doc.get("language") or []) or "unknown"
    rating = doc.get("ratings_average")
    count = doc.get("ratings_count") or 0

    cost = "free" if access in ("public", "borrowable") else "paid/unknown"
    duration = f"{pages} pages" if pages else "unknown"

    lines = [
        f"- [{doc.get('title', 'untitled')}]({url}) — {authors} · {year} · book · "
        f"{duration} · {cost} · verified: mcp:openlibrary {date.today().isoformat()}",
        f"    ebook_access: {access} | languages: {languages}",
    ]
    if isbns:
        lines.append(f"    isbn: {isbns[0]}")
    if rating:
        lines.append(f"    rating: {rating:.2f} from {count} ratings")
    subjects = doc.get("subject") or []
    if subjects:
        lines.append(f"    subjects: {', '.join(subjects[:8])}")
    return "\n".join(lines)


@mcp.tool()
def search_books(query: str, subject: str = "", limit: int = 5) -> str:
    """Search Open Library for books on a topic.

    Use this before recommending any book. Returns real catalogue records with
    Open Library URLs, publication years, page counts and ebook availability,
    already formatted as workflow citations.

    Args:
        query: what to search for, e.g. "spanish grammar for beginners"
        subject: optional subject filter, e.g. "music theory"
        limit: how many results, 1-20
    """
    params: dict[str, str | int] = {
        "q": query,
        "limit": max(1, min(int(limit), 20)),
        "fields": SEARCH_FIELDS,
    }
    if subject:
        params["subject"] = subject

    data = _get("/search.json", params)
    if "__error__" in data:
        return f"ERROR: {data['__error__']}"

    docs = data.get("docs") or []
    if not docs:
        return (f"No Open Library results for {query!r}"
                f"{f' in subject {subject!r}' if subject else ''}. "
                "Broaden the query or use a different source — do not invent a title.")

    header = f"{data.get('numFound', len(docs))} matches, showing {len(docs)}:"
    return header + "\n" + "\n".join(_format(doc) for doc in docs)


@mcp.tool()
def get_book(identifier: str) -> str:
    """Look up one specific book by ISBN (10 or 13 digits) or Open Library ID.

    Use this to confirm a specific edition exists before citing it.

    Args:
        identifier: an ISBN such as "9780521006804", or an OLID such as "OL7353617M"
    """
    clean = identifier.replace("-", "").replace(" ", "").strip()
    if not clean:
        return "ERROR: empty identifier"

    field = "isbn" if clean.isdigit() else "key"
    query = clean if field == "isbn" else f"/works/{clean}" if not clean.startswith("/") else clean

    data = _get("/search.json", {"q": f"{field}:{query}", "limit": 1, "fields": SEARCH_FIELDS})
    if "__error__" in data:
        return f"ERROR: {data['__error__']}"

    docs = data.get("docs") or []
    if not docs:
        return (f"No Open Library record for {identifier!r}. The identifier is wrong or "
                "the edition is not catalogued. Do not cite it.")
    return _format(docs[0])


@mcp.tool()
def browse_subject(subject: str, limit: int = 10) -> str:
    """List well-known works catalogued under a subject.

    Useful early on, to see how a field is actually organised before choosing
    reading for specific modules.

    Args:
        subject: an Open Library subject, e.g. "algebra", "second language acquisition"
        limit: how many works, 1-20
    """
    slug = subject.strip().lower().replace(" ", "_")
    data = _get(f"/subjects/{urllib.parse.quote(slug)}.json",
                {"limit": max(1, min(int(limit), 20))})
    if "__error__" in data:
        return f"ERROR: {data['__error__']}"

    works = data.get("works") or []
    if not works:
        return (f"Open Library has no subject page for {subject!r}. "
                "Try search_books instead, or a broader subject term.")

    lines = [f"Subject '{data.get('name', subject)}' — {data.get('work_count', '?')} works:"]
    for work in works:
        authors = ", ".join(a.get("name", "") for a in work.get("authors") or []) or "unknown"
        lines.append(
            f"- [{work.get('title')}]({API}{work.get('key', '')}) — {authors} · "
            f"{work.get('first_publish_year', 'unknown')} · book · unknown · unknown · "
            f"verified: mcp:openlibrary {date.today().isoformat()}"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
