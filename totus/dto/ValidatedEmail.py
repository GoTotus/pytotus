import json
from enum import Enum
from typing import Dict, Any


class CheckLevel(Enum):
    L1_Syntax = "l1_syntax"
    L2_DNS = "l2_dns"
    L3_Server = "l3_server"
    L4_Dbs = "l4_dbs"

    @classmethod
    def from_string(cls, value: str) -> 'CheckLevel':
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"No CheckLevel enum found for value: {value}")


class ValidatedEmail():
    def __init__(self, _data: Dict[str, Any]):
        self._data = _data

    def email(self) -> str:
        return self._data['email']

    def result(self) -> bool:
        return self._data['result'] == "PASSED"

    def score(self) -> int:
        return self._data['score']

    def mail_servers(self) -> [str]:
        return self._data['mail_servers']

    def requested_level(self) -> CheckLevel:
        return CheckLevel.from_string(self._data['requested_level'])

    def data(self) -> Dict[str, Any]:
        return self._data

    def __repr__(self) -> str:
        """String representation of the object."""
        return json.dumps(self._data, indent=4)
