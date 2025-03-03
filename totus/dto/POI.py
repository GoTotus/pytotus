import json
from typing import Dict, Any


class POI():
    def __init__(self, _data: Dict[str, Any]):
        self._data = _data

    def id(self) -> int:
        """Return the POI's ID."""
        return self._data.get("id", 0)

    def latitude(self) -> float:
        """Return the POI's latitude."""
        return self._data.get("lat", float("nan"))

    def longitude(self) -> float:
        """Return the POI's longitude."""
        return self._data.get("lon", float("nan"))

    def geohash(self) -> str:
        """Return the POI's geohash."""
        return self._data.get("gh")  # None if missing

    def distance(self) -> float:
        """Return the distance to the POI."""
        return self._data.get("dist")  # None if missing

    def info(self) -> Dict[str, str]:
        """Return the POI's associated data."""
        return self._data.get("info", {})

    def __repr__(self) -> str:
        """String representation of the object."""
        return json.dumps({'id': self.id(),
                           'lat': self.latitude(),
                           'lon': self.longitude(),
                           'gh': self.geohash(),
                           'dist': self.distance(),
                           'info': self.info()}, indent=4)
