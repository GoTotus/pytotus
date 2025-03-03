#!/usr/bin/env python3
import json

from totus import Totus

t = Totus()
reference = t.Reference()

print("Public IP:")
print(json.dumps(reference.IP(), indent=4))

print("Google's 8.8.8.8:")
print(json.dumps(reference.IP(ip4='8.8.8.8'), indent=4))

print("Google's ip6 for previous 8.8.8.8: 2001:4860:4860::8888 ...")
print(json.dumps(reference.IP(ip6='2001:4860:4860::8888'), indent=4))
