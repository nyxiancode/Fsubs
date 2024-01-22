# Credits: @mrismanaziz & @Kutmut_Id
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    buttons = [
        [
            InlineKeyboardButton(text="Invitelink", url=client.invitelink),
            InlineKeyboardButton(text="Invitelink2", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton(text="Invitelink3", url=client.invitelink3),
            InlineKeyboardButton(text="Invitelink4", url=client.invitelink4),
        ],
        [
            InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    return buttons

def fsub_button(client, message):
    buttons = [
        [
            InlineKeyboardButton(text="Invitelink", url=client.invitelink),
            InlineKeyboardButton(text="Invitelink2", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton(text="Invitelink3", url=client.invitelink3),
            InlineKeyboardButton(text="Invitelink4", url=client.invitelink4),
        ],
        [
            InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            InlineKeyboardButton(text="Close", callback_data="close"),
        ],
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="Coba Lagi",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ]
        )
    except IndexError:
        pass
    return buttons
