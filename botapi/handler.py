from typing import Callable, List
from botapi.tgtypes import Update


class Handler:
    def __init__(
        self,
        func: Callable[[Update], None],
        rules: Callable[[Update], bool] | List[Callable[[Update], bool]],
    ):
        if isinstance(rules, list):
            self.rules = rules
        else:
            self.rules = [rules]
        self.func = func

    def check(self, update: Update) -> bool:
        for rule in self.rules:
            if not rule(update):
                return False
        return True

    def run(self, update):
        self.func(update)
