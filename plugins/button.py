# Credits: @mrismanaziz & @Kutmut_Id
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    buttons = [
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ],
    ]
    
    if FORCE_SUB_CHANNEL:
        buttons.insert(0, [InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink)])
    if FORCE_SUB_GROUP:
        buttons.insert(1, [InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2)])

    if FORCE_SUB_CHANNEL_2:
        buttons.append([InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3)])
    if FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink4)])

    return buttons

def fsub_button(client, message):
    buttons = []
    
    if FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink)])
    if FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2)])

    if FORCE_SUB_CHANNEL_2:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink3)])
    if FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink4)])

    try:
        buttons.append([
            InlineKeyboardButton(
                text="ᴄᴏʙᴀ ʟᴀɢɪ",
                url=f"https://t.me/{client.username}?start={message.command[1]}",
            )
        ])
    except IndexError:
        pass

    buttons.append([
        InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
    ])

    return buttons
