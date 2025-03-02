import os
import unittest

from totus import Totus


def test_reference_exist():
    assert Totus(api_key='key').Reference() is not None


if __name__ == '__main__':
    unittest.main()
