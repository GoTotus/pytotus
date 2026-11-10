import json
from typing import Dict, Any


class Balance():
    def __init__(self, _data: Dict[str, Any]):
        self._data = _data

    def credits(self) -> float:
        """Return the account balance in credits."""
        return float(self._data.get("credits", 0.0))

    def data(self) -> Dict[str, Any]:
        return self._data

    def __repr__(self) -> str:
        """String representation of the object."""
        return json.dumps(self._data, indent=4)
