import json
from typing import Dict, Any


class Authenticated():
    def __init__(self, _data: Dict[str, Any]):
        self._data = _data

    def authenticated(self) -> bool:
        """Return True if the API key is authenticated."""
        return bool(self._data.get("authenticated", False))

    def description(self) -> str:
        """Return the description confirmation message."""
        return self._data.get("description", "")

    def token_sm(self) -> str:
        """Return the masked short version of the token."""
        return self._data.get("token_sm", "")

    def data(self) -> Dict[str, Any]:
        return self._data

    def __repr__(self) -> str:
        """String representation of the object."""
        return json.dumps(self._data, indent=4)
