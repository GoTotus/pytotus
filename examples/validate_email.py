#!/usr/bin/env python3

from totus import Totus

t = Totus()
validate = t.Validate()

emails = [
    "invalid@gototus.com",
    "sdfsdf@sdfsdfsdfsfs.fdfsfs.fdfsds",
    "temporary@blondmail.com",
    "info@x.com",
    "invalid.email@linkedin.com",
    "info@linkedin.com",
    "support.now@gmail.com"
]

for email in emails:
    result = validate.email(email)
    print(f"email {email}: good email? {'YES' if result.result() else 'NO'}; "
          f"with score: {result.score()}/100")
    print(result)
