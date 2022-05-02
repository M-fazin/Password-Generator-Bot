import random, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Password Generator Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

TEXT = """**Hai {},
I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).**

For Know More /help"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Channel 🔰", url = "https://telegram.me/EKBOTZ_UPDATE"),
            InlineKeyboardButton("Support Group ⭕️", url = "https://telegram.me/ekbotz_support")
        ],
        [
            InlineKeyboardButton("Repo 🗂️", url = "https://github.com/M-fazin/Password-Generator-Bot"),
            InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/M-fazin/Password-Generator-Bot")
        ],
        [
            InlineKeyboardButton("Developer 💡", url = "https://github.com/M-fazin/")
        ]
    ]
)

HELP = """Hai {},
**There Is Nothing To Know More.**

- Send Me The Limit Of Your Password and Keys (optional)
  Like :-
    `10 abcd1234`
    `10`
- I Will Give The Password Of That Limit.

**Note :-**
• Only Digits Are Allowed
• Maximum Allowed Digits Till 100 (I Can't Generate Passwords Above The Length 84)"""

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),
            InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Password-Generator-Bot")
        ]
    ]
)

ABOUT = """--**About Me**--

**🤖 Bot :** Password Generator Bot
**🧑‍💻 Developer :** [M-fazin](https://github.com/M-fazin)
**💻 Channel :** @EKBOTZ_UPDATE
**☎️ Support :** @ekbotz_support
**🗂️ Source Code :** [Password Generator Bot](https://github.com/M-fazin/Password-Generator-Bot)
**⚙️ Language :** Python 3
**🛡️ Framework :** Pyrogram"""


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def password(bot, update):
    
    message = await message.reply_text('`Processing...`')
    
    try:
        if len(update.text.split()) > 1:
            keys, limit = update.text.split()[1], int(update.text.split()[0])
        else:
            keys = "abcdefghijklmnopqrstuvwxyz"+"1234567890"+"!@#$%^&*()_+".lower()
            limit = int(update.text)
    except:
        await message.edit_text('Something wrong')
        return
    
    if limit > 100 or limit <= 0:
        text = "Sorry... Failed To Create Password, Because Limit is 1 to 100."
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @EKBOTZ_UPDATE"
    
    await message.edit_text(text, True)


Bot.run()
