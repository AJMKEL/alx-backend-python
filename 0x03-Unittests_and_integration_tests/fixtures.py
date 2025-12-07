org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
repos_payload = [{"name": "repo1", "license": {"key": "MIT"}},
                 {"name": "repo2", "license": {"key": "BSD"}}]
expected_repos = ["repo1", "repo2"]
apache2_repos = [{"name": "repo1", "license": {"key": "Apache-2.0"}}]
