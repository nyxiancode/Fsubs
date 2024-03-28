from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2
from pyrogram.types import InlineKeyboardButton

def start_button(client):
    buttons = []

    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL != 0:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink)])
    if FORCE_SUB_GROUP and FORCE_SUB_GROUP != 0:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink2)])
    if FORCE_SUB_CHANNEL_2 and FORCE_SUB_CHANNEL_2 != 0:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink3)])
    if FORCE_SUB_GROUP_2 and FORCE_SUB_GROUP_2 != 0:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink4)])

    # Arrange buttons
    arranged_buttons = []

    # If FORCE_SUB_GROUP_2 is 0, arrange buttons accordingly
    if FORCE_SUB_GROUP_2 == 0:
        if buttons:
            arranged_buttons.append(buttons.pop(0))
            if buttons:
                arranged_buttons[0].extend(buttons.pop(0))
        if buttons:
            arranged_buttons.extend(buttons)

    # If FORCE_SUB_GROUP_2 is not 0, no special arrangement needed
    else:
        arranged_buttons = buttons

    arranged_buttons.extend([
        [InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help")],
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ])

    return arranged_buttons

def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink),
                        InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink2)])
    elif FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink)])
    elif FORCE_SUB_GROUP:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink2)])

    if FORCE_SUB_CHANNEL_2 and FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink3),
                        InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink4)])
    elif FORCE_SUB_CHANNEL_2:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink3)])
    elif FORCE_SUB_GROUP_2:
        buttons.append([InlineKeyboardButton(text="ᴊᴏɪɴ💤", url=client.invitelink4)])

    buttons.extend([
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ])

    try:
        buttons.append([InlineKeyboardButton(text="ᴄᴏʙᴀ ʟᴀɢɪ",
                                              url=f"https://t.me/{client.username}?start={message.command[1]}")])
    except IndexError:
        pass

    return buttons
