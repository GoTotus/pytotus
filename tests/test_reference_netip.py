import pprint
import unittest

from totus import Totus


def test_basic_ip():
    r = Totus().Reference().NetIP()
    pprint.pp(r)
    assert r['ip4'] is not None or r['ip6'] is not None


def test_ip4():
    r = Totus().Reference().NetIP(ip4="8.8.8.8")
    assert r['ip4'] == "8.8.8.8"
    assert r['gh'] == "9q9htvvm81jd"


def test_ip6():
    r = Totus().Reference().NetIP(ip6="2001:4860:4860::8888")
    assert r['ip6'] == "2001:4860:4860::8888"
    assert r['gh'] == "9q9htvvm81jd"


if __name__ == '__main__':
    unittest.main()
