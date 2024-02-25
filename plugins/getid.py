from pyrogram import filters, enums
from pyrogram.types import Message

from bot import Bot

@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id

        # Check if the message is a reply
        if message.reply_to_message:
            replied_user_id = message.reply_to_message.from_user.id
            await message.reply_text(
                f"<b>User ID Anda:</b> <code>{user_id}</code>\n<b>Replied User ID:</b> <code>{replied_user_id}</code>",
                quote=True
            )
        else:
            await message.reply_text(
                f"<b>User ID Anda:</b> <code>{user_id}</code>",
                quote=True
            )
