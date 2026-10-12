from datetime import datetime, timezone
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from scholarly import scholarly


OUTPUT_DIR = Path("results")
OUTPUT_DIR.mkdir(exist_ok=True)


def fetch_json(url, headers=None):
    if not url:
        return None
    request_headers = {"User-Agent": "wzwvv.github.io profile metrics updater"}
    if headers:
        request_headers.update(headers)
    request = Request(url, headers=request_headers)
    try:
        with urlopen(request, timeout=45) as response:
            return json.load(response)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as error:
        print(f"Could not load {url}: {error}")
        return None


def write_json(filename, payload):
    with (OUTPUT_DIR / filename).open("w", encoding="utf-8") as outfile:
        json.dump(payload, outfile, ensure_ascii=False, indent=2)


def fetch_google_scholar(author_id, cached_author):
    try:
        author = scholarly.search_author_id(author_id)
        scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
        author["updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        author["publications"] = {
            publication["author_pub_id"]: publication
            for publication in author.get("publications", [])
        }
        return author
    except Exception as error:  # Scholar may temporarily rate-limit automated requests.
        print(f"Google Scholar update failed; using the latest cached value: {error}")
        return cached_author or {}


def fetch_github_totals(username, token):
    total_stars = 0
    repository_count = 0
    page = 1
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    while True:
        query = urlencode({"per_page": 100, "page": page, "type": "owner", "sort": "full_name"})
        repositories = fetch_json(
            f"https://api.github.com/users/{username}/repos?{query}",
            headers=headers,
        )
        if not repositories:
            break
        total_stars += sum(int(repository.get("stargazers_count", 0)) for repository in repositories)
        repository_count += len(repositories)
        if len(repositories) < 100:
            break
        page += 1

    return total_stars, repository_count


def fetch_zenodo_totals(record_id):
    record = fetch_json(f"https://zenodo.org/api/records/{record_id}") or {}
    stats = record.get("stats", {})
    return stats.get("downloads"), stats.get("unique_downloads")


now = datetime.now(timezone.utc)
updated_at = now.isoformat(timespec="seconds")
repository = os.environ.get("GITHUB_REPOSITORY", "wzwvv/wzwvv.github.io")
github_username = os.environ.get("GITHUB_USERNAME", "wzwvv")
scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "fjlXqvQAAAAJ")
zenodo_record_id = os.environ.get("ZENODO_RECORD_ID", "19333249")

metrics_cache_url = os.environ.get(
    "METRICS_CACHE_URL",
    f"https://raw.githubusercontent.com/{repository}/google-scholar-stats/profile_metrics.json",
)
scholar_cache_url = os.environ.get(
    "SCHOLAR_CACHE_URL",
    f"https://raw.githubusercontent.com/{repository}/google-scholar-stats/gs_data.json",
)

cached_metrics = fetch_json(metrics_cache_url) or {}
cached_author = fetch_json(scholar_cache_url) or {}
author = fetch_google_scholar(scholar_id, cached_author)

github_stars, github_repositories = fetch_github_totals(
    github_username,
    os.environ.get("GITHUB_TOKEN", ""),
)
if github_repositories == 0 and cached_metrics.get("github_repositories"):
    github_stars = cached_metrics.get("github_stars")
    github_repositories = cached_metrics.get("github_repositories")

# Zenodo changes more slowly than Scholar citations and GitHub stars. Refresh it
# every Monday, while retaining the latest cached value on other days.
refresh_zenodo = now.weekday() == 0 or cached_metrics.get("zenodo_downloads") is None
if refresh_zenodo:
    zenodo_downloads, zenodo_unique_downloads = fetch_zenodo_totals(zenodo_record_id)
    if zenodo_downloads is None:
        zenodo_downloads = cached_metrics.get("zenodo_downloads")
        zenodo_unique_downloads = cached_metrics.get("zenodo_unique_downloads")
        zenodo_updated = cached_metrics.get("zenodo_updated")
    else:
        zenodo_updated = updated_at
else:
    zenodo_downloads = cached_metrics.get("zenodo_downloads")
    zenodo_unique_downloads = cached_metrics.get("zenodo_unique_downloads")
    zenodo_updated = cached_metrics.get("zenodo_updated")

profile_metrics = {
    "google_scholar_citations": author.get(
        "citedby", cached_metrics.get("google_scholar_citations")
    ),
    "google_scholar_url": f"https://scholar.google.com/citations?user={scholar_id}&hl=en",
    "github_stars": github_stars,
    "github_repositories": github_repositories,
    "github_url": f"https://github.com/{github_username}?tab=repositories",
    "zenodo_downloads": zenodo_downloads,
    "zenodo_unique_downloads": zenodo_unique_downloads,
    "zenodo_url": f"https://zenodo.org/records/{zenodo_record_id}",
    "updated": updated_at,
    "zenodo_updated": zenodo_updated,
    "update_frequency": {
        "google_scholar": "daily",
        "github": "daily",
        "zenodo": "weekly",
    },
}

if author:
    write_json("gs_data.json", author)

write_json("profile_metrics.json", profile_metrics)
write_json(
    "gs_data_shieldsio.json",
    {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(profile_metrics.get("google_scholar_citations") or "unavailable"),
    },
)

print(json.dumps(profile_metrics, ensure_ascii=False, indent=2))
