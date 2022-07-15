import json
from urllib.request import urlopen
from urllib.parse import urlencode
from typing import Any


class HTTPClient:
    @staticmethod
    def request(url: str, **data: Any) -> dict:
        encode_data = urlencode(data).encode()
        with urlopen(url=url, data=encode_data) as response:
            return json.loads(response.read())
