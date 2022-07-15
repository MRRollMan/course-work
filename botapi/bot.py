import typing
from botapi.api import API as APIClient
from botapi.handler import Handler
from botapi.tgtypes import Update


class Bot:
    __handlers: typing.List[Handler] = []
    _run: bool = False

    def __init__(self, token: str):
        self.__botToken = token
        self.API = APIClient(self.__botToken)

    def add_handler(self, handler: Handler):
        self.__handlers.append(handler)

    def start_polling(self, offset=0):
        self._run = True
        while self._run:
            for update in self._get_updates(offset):
                offset = self._process_update(update)

    def _get_updates(self, offset: int) -> list[Update]:
        return self.API.get_updates(offset=offset, allowed_updates=["message"])

    def _process_update(self, update: Update) -> int:
        handler = self._check_handlers(update)
        if handler is not None:
            handler.run(update)
        return update.update_id + 1

    def _check_handlers(self, update: Update) -> Handler|None:
        for handler in self.__handlers:
            if handler.check(update):
                return handler
        return None
