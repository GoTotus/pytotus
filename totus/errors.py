from typing import Optional


# Custom Exceptions
class TotusClientError(Exception):
    """Base exception for all Totus Client related errors."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{message} (Status: {status_code})" if status_code else message)


class AuthenticationError(TotusClientError):
    """Raised when authentication fails (e.g., invalid bearer token)."""


class NotFoundError(TotusClientError):
    """Raised when a resource is not found (HTTP 404). Possibly an old client. """


class ClientError(TotusClientError):
    """Raised for client-side errors (HTTP 4xx, excluding 401/404)."""


class ServerError(TotusClientError):
    """Raised for server-side errors (HTTP 5xx)."""
