from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import Config
from ..screenshotbot import ScreenShotBot
from bot.database.forcesub import ForceSub


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m, cb=False):
    forcesub = await ForceSub(c, m)
    if forcesub == 400:
        return
    owner_id = Config.AUTH_USERS[0]
    username = 'TheTeleRoid'
    mention = '[Pʀᴇᴅ∆ᴛᴏʀ](https://t.me/ArkBotz)'
    try:
        owner = await c.get_users(owner_id)
        username = owner.username if owner.username else 'PredatorHackerzZ'
        mention = owner.mention(style="md")
    except Exception as e:
        print(e)

    BUTTONS = [[
        InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
        InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
        ],[
        InlineKeyboardButton("Updates", url="https://t.me/ARKBotz")
    ]]

    TEXT = f"👋 Hey {m.from_user.mention},\n\nI'm Screenshot as well as Sample Generator Bot. I can provide screenshots, sample video from "
    TEXT += "your medias and also can trim. For more details check /help.\n\n"

    if cb:
        try:
            await m.message.edit(
                text=TEXT,
                reply_markup=InlineKeyboardMarkup(BUTTONS)
            )
        except:
            pass
    else:
        await m.reply_text(
            text=TEXT,
            quote=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )


# i generally liked to use regex filters for callback 
# but since odysseusmax used lambda i am also using the same
@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("home"))
)
async def home_cb(c, m):
    await m.answer()
    await start(c, m, True)


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("close"))
)
async def close_cb(c, m):
    try:
        await m.message.delete()
        await m.message.reply_to_message.delete()
    except:
        pass
