from botapi.tgtypes import Update


def startFunc(update: Update):
    user_fn = update.message.from_user.first_name
    text = f"Привіт, {user_fn}!\nЯк у тебе справи❓"
    cid = update.message.chat.id
    update.API.send_message(chat_id=cid, text=text)


def moodFunc(update: Update):
    cid = update.message.chat.id
    update.API.send_message(chat_id=cid, text=update.payload.get("answer"))


def testFunc(update: Update):
    cid = update.message.chat.id
    args: list = update.payload.get("args", [])
    if len(args) > 1:
        update.API.send_message(chat_id=cid, text="\n".join(args[1:]))
    else:
        update.API.send_message(chat_id=cid, text="test")


def settingFunc(update: Update):
    update.API.send_message(chat_id=update.message.chat.id, text=str(update.message))
