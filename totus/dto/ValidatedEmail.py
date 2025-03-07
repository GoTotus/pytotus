import json
from typing import Dict, Any


class ValidatedEmail():
    def __init__(self, _data: Dict[str, Any]):
        self._data = _data

    def email(self) -> str:
        return self._data['email']

    def result(self) -> bool:
        return self._data['result'] == "PASSED"

    def mail_servers(self) -> [str]:
        return self._data['mail_servers']

    def data(self) -> Dict[str, Any]:
        return self._data

    def __repr__(self) -> str:
        """String representation of the object."""
        return json.dumps(self._data, indent=4)
