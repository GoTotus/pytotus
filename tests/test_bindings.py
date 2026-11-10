import os
import unittest

from totus import Totus


def test_reference_exist():
    assert Totus(api_key='key').Reference() is not None


def test_balance_exist():
    t = Totus(api_key='key')
    assert hasattr(t, 'balance')
    assert hasattr(t, 'Balance')
    assert hasattr(t, 'authenticated')
    assert hasattr(t, 'Authenticated')
    assert t.Utility() is not None



if __name__ == '__main__':
    unittest.main()
