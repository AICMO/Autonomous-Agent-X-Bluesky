"""Offline checks for the legacy client's TLS policy."""

import importlib.util
import os
from pathlib import Path
import unittest
from unittest.mock import patch
import warnings

from urllib3.exceptions import InsecureRequestWarning


CLIENT_PATH = Path(__file__).resolve().parents[1] / "x.py"
TEST_ENV = {
    "X_API_KEY": "test-consumer-key",
    "X_API_KEY_SECRET": "test-consumer-secret",
    "X_ACCESS_TOKEN": "test-access-token",
    "X_ACCESS_TOKEN_SECRET": "test-access-secret",
}


def load_client():
    spec = importlib.util.spec_from_file_location("legacy_x_client", CLIENT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TlsPolicyTests(unittest.TestCase):
    def test_direct_and_proxy_requests_verify_certificates(self):
        for proxy_var in (None, "HTTPS_PROXY", "https_proxy"):
            with self.subTest(proxy_var=proxy_var):
                env = dict(TEST_ENV)
                if proxy_var:
                    env[proxy_var] = "http://proxy.example:8080"
                with patch.dict(os.environ, env, clear=True):
                    with load_client().get_oauth_session() as session:
                        settings = session.merge_environment_settings(
                            "https://api.twitter.com/2/users/me", {}, False, None, None
                        )
                        self.assertIs(settings["verify"], True)
                        if proxy_var:
                            self.assertEqual(
                                settings["proxies"]["https"], env[proxy_var]
                            )

    def test_explicit_ca_bundle_is_used_with_proxy(self):
        env = {
            **TEST_ENV,
            "HTTPS_PROXY": "http://proxy.example:8080",
            "REQUESTS_CA_BUNDLE": "/test/trusted-ca-bundle.pem",
        }
        with patch.dict(os.environ, env, clear=True):
            with load_client().get_oauth_session() as session:
                settings = session.merge_environment_settings(
                    "https://api.twitter.com/2/users/me", {}, False, None, None
                )
                self.assertEqual(settings["verify"], env["REQUESTS_CA_BUNDLE"])

    def test_import_does_not_hide_insecure_request_warnings(self):
        with warnings.catch_warnings(record=True) as recorded:
            warnings.simplefilter("always", InsecureRequestWarning)
            load_client()
            warnings.warn("TLS regression check", InsecureRequestWarning)
        self.assertEqual(len(recorded), 1)
        self.assertIs(recorded[0].category, InsecureRequestWarning)


if __name__ == "__main__":
    unittest.main()
