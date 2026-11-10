#!/usr/bin/env python3
from totus import Totus

t = Totus()  # Picks up key from TOTUS_KEY environment variable

balance = t.balance()
print(f"Account Balance: {balance.credits():.2f} Credits")
print(balance)
