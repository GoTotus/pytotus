import json
import math

from totus.dto.POI import POI


class Reference():

    def __init__(self, _totus):
        self._totus = _totus

    def GeoPOI(self,
               lat: float = math.nan, lon: float = math.nan, gh: str = None,
               what: str = None,
               distance: float = None,
               filter: dict[str, str] = None,
               limit: int = None,
               ) -> [dict]:
        params: dict[str, any] = {}
        if not math.isnan(lat) and not math.isnan(lon):
            params['lat'] = lat
            params['lon'] = lon
        if gh is not None:
            params['gh'] = gh
        if what is not None:
            params['what'] = what
        if distance is not None:
            params['dist'] = distance
        if filter is not None:
            params['filter'] = [f"{k}={v}" for k, v in filter.items()]
            for k, v in filter.items():
                params["filter"] = f"{k}={v}"
        if limit is not None:
            params['limit'] = limit

        response = self._totus._make_request('GET', '/ref/geo/poi', params)
        return [POI(item) for item in response]

    def IP(self, ip4=None, ip6=None):
        params: dict[str, any] = {}
        if ip4:
            params['ip4'] = ip4
        elif ip6:
            params['ip6'] = ip6
        return self._totus._make_request('GET', '/ref/ip', params)
