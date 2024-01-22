# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import OWNER
from REA import Data  # changed import statement
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message


@Bot.on_message(filters.private & filters.incoming & filters.command("order"))  # changed command to "order"
async def _order(client: Bot, msg: Message):  # changed function name
    await client.send_message(
        msg.chat.id,
        Data.ORDER.format(client.username, OWNER),  # changed format string
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.mbuttons),
    )


@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        "<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "order":  # changed callback data to "order"
        try:
            await query.message.edit_text(
                text=Data.ORDER.format(client.username, OWNER),  # changed format string
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.mbuttons),
            )
        except MessageNotModified:
            pass
    elif data == "help":
        try:
            await query.message.edit_text(
                text="<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
