import unittest
from unittest.mock import MagicMock

from totus import Totus


class TestBalance(unittest.TestCase):

    def test_balance_success(self):
        t = Totus(api_key="test-api-key")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"credits": 1234.56}
        t.session.request = MagicMock(return_value=mock_response)

        # Direct call
        bal = t.balance()
        t.session.request.assert_called_with('GET', 'https://api.totus.cloud/balance', params=None, json=None)
        self.assertEqual(bal.credits(), 1234.56)
        self.assertIn("1234.56", repr(bal))

        # Uppercase alias
        bal2 = t.Balance()
        self.assertEqual(bal2.credits(), 1234.56)

        # Via Utility()
        util_bal = t.Utility().balance()
        self.assertEqual(util_bal.credits(), 1234.56)

    def test_utility_exists(self):
        t = Totus(api_key="test-api-key")
        self.assertIsNotNone(t.Utility())

    def test_authenticated_success(self):
        t = Totus(api_key="test-api-key")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "authenticated": True,
            "description": "your api_key is working",
            "token_sm": "TTT_123...456"
        }
        t.session.request = MagicMock(return_value=mock_response)

        # Via Utility()
        auth = t.Utility().authenticated()
        t.session.request.assert_called_with('GET', 'https://api.totus.cloud/authenticated', params=None, json=None)
        self.assertTrue(auth.authenticated())
        self.assertEqual(auth.description(), "your api_key is working")
        self.assertEqual(auth.token_sm(), "TTT_123...456")
        self.assertIn("your api_key is working", repr(auth))

        # Direct on client
        auth_direct = t.authenticated()
        self.assertTrue(auth_direct.authenticated())



if __name__ == '__main__':
    unittest.main()
