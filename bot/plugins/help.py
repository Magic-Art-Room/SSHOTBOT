from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


HELP_TEXT = """
**Usage Instructions**

Just Send me any File and after downloading complete it will show you some options like Screenshot or Trim or Sample and you have to choose one. 

See /settings to configure bot's behavior.
Use /set_watermark to set custom watermarks to your screenshots.

**Bot Managed By @ARKBotz**
"""

@ScreenShotBot.on_message(filters.private & filters.command("help"))
async def help_(c, m):

    await m.reply_text(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("help"))
)
async def help_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS)
    )
