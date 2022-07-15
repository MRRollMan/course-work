import os
from botapi.bot import Bot
from botapi.handler import Handler
from botapi.tgtypes import Update
from .rules import moodRule, startRule, commandRule, settingsRule, orRule
from .funcs import moodFunc, startFunc, testFunc, settingFunc

bot = Bot(os.getenv("WTBOT_TOKEN") or "")

me = bot.API.get_me()

print(f"{me.first_name}({me.id}|@{me.username})")

bot.add_handler(Handler(startFunc, startRule))
bot.add_handler(Handler(moodFunc, moodRule))
bot.add_handler(
    Handler(testFunc, orRule(*[commandRule("test", prefix=p) for p in ["/", ".", "!"]]))
)
bot.add_handler(Handler(settingFunc, settingsRule))


try:
    bot.start_polling()
except KeyboardInterrupt:
    pass
