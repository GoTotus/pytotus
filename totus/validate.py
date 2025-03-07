from enum import Enum

from totus.dto.ValidatedEmail import ValidatedEmail


class Validate():
    def __init__(self, _totus):
        self._totus = _totus

    class EmailCheckLevel(Enum):
        L1_Syntax = "l1_syntax"
        L2_DNS = "l2_dns"
        L3_Server = "l3_server"
        L4_Dbs = "l4_dbs"

    def email(self, email: str, level: EmailCheckLevel = EmailCheckLevel.L4_Dbs) -> ValidatedEmail:
        return ValidatedEmail(self._totus._make_request('GET', '/validate/email', {'email': email, 'level': level.value}))
