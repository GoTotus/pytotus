#!/usr/bin/env python3
import json

from totus import Totus

t = Totus()
reference = t.Reference()

print("Your Public IP ...")
result = reference.NetIP()
print(json.dumps(result, indent=4))

print("Cloudflare 1.1.1.1 ...")
result = reference.NetIP(ip4='1.1.1.1')
print(json.dumps(result, indent=4))

print("Cloudflare ip6 for previous 1.1.1.1: 2606:4700:4700::1111 ...")
result = reference.NetIP(ip6='2606:4700:4700::1111')
print(json.dumps(result, indent=4))
