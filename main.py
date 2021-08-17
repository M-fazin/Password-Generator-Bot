# Author M_fazin <github.com/M-fazin>

from pyrogram import  Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


import random
import os


Ek = Client(
    "Password Generator Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

@Ek.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
        TEXT = "Hai {} \n\n**I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).** \n\nFor Know More /help"
        BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel 🔰", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("Support Group ⭕️", url = "https://telegram.me/ekbotz_support")],[InlineKeyboardButton("Repo 🗂️", url = "https://github.com/M-fazin/Password-Generator-Bot"),InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/M-fazin/Password-Generator-Bot")],[InlineKeyboardButton("Developer 💡", url = "https://github.com/M-fazin/")]])
        await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
	
@Ek.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
        HELP = "Hai {} \n\n**There Is Nothing To Know More.** \n- Send Me The Limit Of Your Password \n- I Will Give The Password Of That Limit. \n\nEx:- `20` \n\n**Note :-**\n• Only Digits Are Allowed \n• Maximum Allowed Digits Till 84 (I Can't Generate Passwords Above The Length 84)"
        HELP_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Password-Generator-Bot")]])
        await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@Ek.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
	ABOUT = "**🤖 Bot :** Password Generator Bot\n\n**🧑‍💻 Developer :** [M-fazin](https://github.com/M-fazin)\n\n**💻 Channel :** @EKBOTZ_UPDATE\n\n**☎️ Support :** @ekbotz_support \n\n**🗂️ Source Code :** [Password Generator Bot](https://github.com/M-fazin/Password-Generator-Bot)\n\n**⚙️ Language :** Python 3\n\n**🛡️ Framework :** Pyrogram"
	await update.reply_text(
	text=ABOUT,
	disable_web_page_preview=True,
	quote=True
	)
	
@Ek.on_message(filters.private & filters.text)
async def password(bot, message):
    password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
    try:
    limit = int(message.text)
    except:
        pass    
    if limit >= 85 or limit <= 0:
        text = "Sorry... Failed To Create Password Because Limit is 1 to 84"
    else:
        randomValue = random.sample(password, limit)
        randomValue = "".join(randomValue)
        text = f"**Your Password Generated Succesfully.** \nYour Password Limit : `{limit}`. \nPassword 👇 :- \n`{randomValue}` \n\n**Join @EKBOTZ_UPDATE"
        await message.reply_text(text, True)
			

			
Ek.run()
