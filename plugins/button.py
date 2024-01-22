from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons

def fsub_button(client, message):
    buttons = []
    
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ]
        )
        buttons.extend(
            [
                [
                    InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                    InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
                ],
                [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
            ]
        )

    if FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons.append(
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ]
        )
        buttons.extend(
            [
                [
                    InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
                    InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink4),
                ],
                [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
            ]
        )

    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ]
        )
    except IndexError:
        pass

    return buttons
