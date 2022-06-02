from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config
from bot.database.forcesub import ForceSub


BUTTONS = [[
    InlineKeyboardButton('🏡 Home', callback_data='home'),
    InlineKeyboardButton('🚸 Powered By', url='t.me/MoviesFlixers_DL'),
    InlineKeyboardButton('♻ Help', callback_data='help')
]]

ABOUT_TEXT = """
╭────[🔅Sᴄʀᴇᴇɴsʜᴏᴛ Bᴏᴛ🔅]───⍟
│
├<b>🤖 My Name : <a href='https://t.me/ArkSampleSSBot'>Sample and SS Bot</a></b>
│
├<b>🌐 Hosted on : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://docs.pyrogram.org'>Pyrogram</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://t.me/settings'>All Contributors</a></b>
│
├<b>📢 Channel : <a href='https://t.me/ARKBotz'>ArkBotz</a></b>
│
╰────────[Thank You]───⍟

"""

@ScreenShotBot.on_message(filters.private & filters.command("about"))
async def about_(c, m):
    forcesub = await ForceSub(c, m,)
    if forcesub == 400:
        return
    await m.reply_text(
        text=ABOUT_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("about"))
)
async def about_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=ABOUT_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS)
    )
