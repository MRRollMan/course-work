from typing import Callable
from botapi.tgtypes import Update


def startRule(update: Update) -> bool:
    return commandRule("start")(update)


def helpRule(update: Update) -> bool:
    return commandRule("help", False)(update)


def settingsRule(update: Update) -> bool:
    return commandRule("settings", False)(update)


def moodRule(update: Update) -> bool:
    if update.message.text is None:
        return False
    mood = ["погано", "непогано", "добре", "чудово"]
    text = update.message.text.lower()
    if not (text in mood):
        return False
    answer = [
        "Сподіваюсь, що завтра у тебе все буде чудово!🤗",
        "Ну це краще, ніж могло би бути😌",
        "Я дуже радий за тебе😀",
        "Че ж чудово!!😜😜",
    ]
    update.payload["answer"] = answer[mood.index(text)]
    return True


def commandRule(
    text: str, has_args: bool = True, prefix="/"
) -> Callable[[Update], bool]:
    def run(update: Update) -> bool:
        if update.message.text is None:
            return False
        update.payload["args"] = update.message.text.split()
        if not has_args:
            return update.message.text.lower() == f"{prefix}{text}"
        return update.message.text.lower().startswith(f"{prefix}{text}")

    return run


def orRule(*rules: Callable[[Update], bool]) -> Callable[[Update], bool]:
    def run(update: Update) -> bool:
        return any(map(lambda f: f(update), rules))

    return run


def allRule(*rules: Callable[[Update], bool]) -> Callable[[Update], bool]:
    def run(update: Update) -> bool:
        return all(map(lambda f: f(update), rules))

    return run


def notRule(rule: Callable[[Update], bool]) -> Callable[[Update], bool]:
    def run(update: Update) -> bool:
        return not rule(update)

    return run
