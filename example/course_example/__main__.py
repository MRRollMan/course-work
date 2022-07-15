import os
from botapi.bot import Bot
from botapi.handler import Handler
from botapi.tgtypes import Update

def main():
    bot.add_handler(Handler(startFunc, startRule))
    bot.add_handler(Handler(helloFunc, lambda upd: upd.message.text == '/hello'))
    bot.add_handler(Handler(echoFunc, lambda _: True))
    bot.start_polling()

def startFunc(update: Update):
    text = f"Вітаю!\nВи скористались командою /start"
    update.API.send_message(chat_id=update.message.chat.id, text=text)

def helloFunc(update: Update):
    text = f"Привіт, {update.message.from_user.first_name}!"
    update.API.send_message(chat_id=update.message.chat.id, text=text)

def echoFunc(update: Update):
    update.API.send_message(chat_id=update.message.chat.id, text=f'Ви написали "{update.message.text}"')

def startRule(update: Update) -> bool: return update.message.text == '/start'

if __name__ == '__main__':
    bot = Bot(os.getenv("WTBOT_TOKEN") or '' )
    main()