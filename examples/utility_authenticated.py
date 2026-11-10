#!/usr/bin/env python3
from totus import Totus

t = Totus()  # Picks up key from TOTUS_KEY environment variable

auth = t.authenticated()
print(f"Authenticated: {auth.authenticated()}")
print(f"Description: {auth.description()}")
print(f"Token (masked): {auth.token_sm()}")
print(auth)
