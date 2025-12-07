#!/usr/bin/env python3
"""Github client"""

from utils import get_json

class GithubOrgClient:
    """Github organization client"""

    def __init__(self, org_name):
        self.org_name = org_name
        self._public_repos_url = None

    @property
    def org(self):
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

    def _public_repos_url(self):
        return self.org["repos_url"]

    def public_repos(self):
        url = self._public_repos_url()
        repos = get_json(url)
        return [repo["name"] for repo in repos]

    def has_license(self, repo, license_key):
        return repo.get("license", {}).get("key") == license_key
