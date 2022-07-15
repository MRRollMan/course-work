from typing import Any

from botapi.http_client import HTTPClient
from botapi.tgtypes import User, Message, Update


class APIClient:
    _http = HTTPClient
    _api_url = "https://api.telegram.org/bot{token}/"

    def __init__(self, token: str):
        self._api_url = self._api_url.format(token=token)

    def request(self, method: str, **kwargs: Any) -> dict:
        return self._http.request(self._api_url + method, **kwargs)["result"]


class API(APIClient):
    def __init__(self, token: str):
        super().__init__(token)

    def get_me(self) -> User:
        return User(**self.request("getMe"))

    def send_message(self, **kwargs) -> Message:
        return Message.from_telegram(self.request("sendMessage", **kwargs))

    def get_updates(self, **kwargs) -> list[Update]:
        r = self.request("getUpdates", **kwargs)
        return [Update(**upd, API=self) for upd in r]
