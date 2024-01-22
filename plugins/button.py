# Credits: @mrismanaziz & @Kutmut_Id
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Invite Link", url=client.invitelink),
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [InlineKeyboardButton(text="Group", url=client.invitelink2)],
            [
                InlineKeyboardButton(text="Invite Link", url=client.invitelink),
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [InlineKeyboardButton(text="Channel", url=client.invitelink)],
            [
                InlineKeyboardButton(text="Invite Link", url=client.invitelink),
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink),
                InlineKeyboardButton(text="Group", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [InlineKeyboardButton(text="Join Group", url=client.invitelink2)],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [InlineKeyboardButton(text="Join Channel", url=client.invitelink)],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Join Channel", url=client.invitelink),
                InlineKeyboardButton(text="Join Group", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    if not FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons = [
            [InlineKeyboardButton(text="Group", url=client.invitelink4)],
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_2 and not FORCE_SUB_GROUP_2:
        buttons = [
            [InlineKeyboardButton(text="Channel", url=client.invitelink3)],
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons = [
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Channel", url=client.invitelink3),
                InlineKeyboardButton(text="Group", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons
