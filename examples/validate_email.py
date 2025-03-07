#!/usr/bin/env python3

import json

from totus import Totus

t = Totus()
validate = t.Validate()

emails = ["invalid@gototus.com",
          "temporary@blondmail.com",
          "info@x.com",
          "fdsladskjfkfsklhfls@linkedin.com",
          "info@linkedin.com"]
for email in emails:
    print(email, "...")
    print(validate.email(email))
