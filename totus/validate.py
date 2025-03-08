from enum import Enum

from totus.dto.ValidatedEmail import ValidatedEmail, CheckLevel


class Validate():
    def __init__(self, _totus):
        self._totus = _totus


    def email(self, email: str, level: CheckLevel = CheckLevel.L4_Dbs) -> ValidatedEmail:
        return ValidatedEmail(self._totus._make_request('GET', '/validate/email', {'email': email, 'level': level.value}))
