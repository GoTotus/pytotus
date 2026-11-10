from .dto.Balance import Balance
from .dto.Authenticated import Authenticated


class Utility():
    def __init__(self, _totus):
        self._totus = _totus

    def balance(self) -> Balance:
        return self._totus.balance()

    def Balance(self) -> Balance:
        return self.balance()

    def authenticated(self) -> Authenticated:
        response = self._totus._make_request('GET', '/authenticated')
        return Authenticated(response)

    def Authenticated(self) -> Authenticated:
        return self.authenticated()
