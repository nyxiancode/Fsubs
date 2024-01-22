# Credits: @mrismanaziz & @Kutmut_Id
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    buttons = []

    if FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink)])
    if FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2)])
    if FORCE_SUB_CHANNEL_2:
        buttons.append([InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3)])
    if FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink4)])

    buttons.extend([
        [InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help")],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ])

    return buttons

def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                        InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2)])
    elif FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink)])
    elif FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2)])

    if FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3),
                        InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink4)])
    elif FORCE_SUB_CHANNEL_2:
        buttons.append([InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink3)])
    elif FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink4)])

    buttons.extend([
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ])

    try:
        buttons.append([InlineKeyboardButton(text="ᴄᴏʙᴀ ʟᴀɢɪ",
                                              url=f"https://t.me/{client.username}?start={message.command[1]}")])
    except IndexError:
        pass

    return buttons
