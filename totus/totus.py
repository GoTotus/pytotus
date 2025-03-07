import os
from typing import Optional, Dict, Any

import requests

from .errors import AuthenticationError, ClientError, TotusClientError, ServerError, NotFoundError
from .reference import Reference
from .validate import Validate


class Totus():

    def __init__(self,
                 api_key: Optional[str] = None,
                 endpoint: str = "https://api.totus.cloud",
                 proxy: Optional[str] = None
                 ):
        """Initialize Totus API, can provide an API key (default from env var), base URL and a proxy."""
        self.api_key = api_key or os.getenv("TOTUS_KEY")
        if not self.api_key:
            raise TotusClientError("API Key must be provided or set in TOTUS_KEY environment variable")
        self.base_url = endpoint.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        if proxy:
            self.session.proxies.update({'https': proxy})

    def _make_request(self,
                      method: str,
                      endpoint: str,
                      params: Optional[Dict[str, any]] = None,
                      data: Optional[Dict] = None) -> Dict[str, Any]:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            try:
                error_data = e.response.json()
                message = error_data.get("error", "Unknown error")
            except (ValueError, AttributeError):
                message = e.response.text or "Unknown error"
            if status == 401:
                raise AuthenticationError(message, status)
            elif status == 404:
                raise NotFoundError(f"Resource not found: {url}", status)
            elif 400 <= status < 500:
                raise ClientError(f"Bad request: {message}", status)
            elif 500 <= status < 600:
                raise ServerError(f"Server error: {message}", status)
            else:
                raise TotusClientError(f"Unexpected HTTP error: {message}", status) from e
        except requests.exceptions.RequestException as e:
            raise TotusClientError(f"Network error: {str(e)}")

    def Reference(self) -> Reference:
        return Reference(self)

    def Validate(self) -> Validate:
        return Validate(self)