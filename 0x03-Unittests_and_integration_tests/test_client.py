#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos

class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        mock_get_json.return_value = org_payload
        client = GithubOrgClient("google")
        self.assertEqual(client.org, org_payload)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        mock_get_json.return_value = repos_payload
        client = GithubOrgClient("google")
        client._public_repos_url = lambda: "mock_url"
        self.assertEqual(client.public_repos(), expected_repos)

    def test_has_license(self):
        client = GithubOrgClient("google")
        repo = {"license": {"key": "MIT"}}
        self.assertTrue(client.has_license(repo, "MIT"))
        self.assertFalse(client.has_license(repo, "BSD"))
