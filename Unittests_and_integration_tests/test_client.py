#!/usr/bin/env python3
"""A module for client tests"""

from utils import get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
	"""test GithubOrgClient"""
	
	@parameterized.expand([
		("google",),
		("abc",),
	])
	@patch("client.get_json")
	def test_org(self, org_name, mock_get_json):
		"""assures org returns correct value"""

		expected = {"login": org_name}
		mock_get_json.return_value = expected

		client = GithubOrgClient
		result = client.org

		self.assertEqual(result, expected)

		mock_get_json.assert_called_once_with(
			f"https://api.github.com/orgs/{org_name}"
		)
