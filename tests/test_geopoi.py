import os
import pprint
import unittest

from totus import Totus


def test_basic_geopoi():
    r = (Totus().Reference().GeoPOI(gh='69y7pkxfc', distance=1000, what='shop', limit=10))
    pprint.pp(r[0].info())
    assert len(r) == 10


if __name__ == '__main__':
    unittest.main()
