# (©)Codexbotz
# Recode By Zaen @Mafia_Tobatz
# Recode By Dappa @mahadappa
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod

import asyncio
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, FORCE_MSG, START_MSG, PROTECT_CONTENT
from database.sql import add_user, full_userbase, query_msg
from helper_func import decode, get_messages, subscribed

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Bot.on_message(filters.command("start") & filters.private & subscribed)
async def start_command(client: Bot, message: Message):
    id = message.from_user.id
    user_name = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else None
    )

    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except BaseException:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except BaseException:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except BaseException:
                return
        temp_msg = await message.reply("<code>Tunggu Sebentar...</code>")
        try:
            messages = await get_messages(client, ids)
        except BaseException:
            await message.reply_text("<b>Telah Terjadi Error </b>🥺")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(
                    previouscaption=msg.caption if msg.caption else "",
                    filename=msg.document.file_name,
                )

            else:
                caption = msg.caption if msg.caption else ""

            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None
            try:
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode=None,  # Remove parse_mode "html"
                    protect_content=PROTECT_CONTENT,
                    reply_markup=reply_markup,
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode=None,  # Remove parse_mode "html"
                    protect_content=PROTECT_CONTENT,
                    reply_markup=reply_markup,
                )
            except BaseException:
                pass
    else:
        buttons = [
                [
                    InlineKeyboardButton("Cara Penggunaan", callback_data="help"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
                ]
            ]
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None
                if not message.from_user.username
                else "@" + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
            quote=True,
        )

    return


@Bot.on_message(filters.command("start") & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("•ᴄʜᴀɴᴇʟ•", url=client.invitelink1), 
            InlineKeyboardButton("•ᴄʜᴀɴᴇʟ•", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton("•ᴄʜᴀɴᴇʟ•", url=client.invitelink3), 
            InlineKeyboardButton("•ᴄʜᴀɴᴇʟ•", url=client.invitelink4),
        ],
    ]
    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="•ᴄᴏʙᴀ ʟᴀɢɪ•",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ]
        )
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None
            if not message.from_user.username
            else "@" + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command("users") & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(
        chat_id=message.chat.id, text="<code>Processing ...</code>"
    )
    users = await full_userbase()
    await msg.edit(f"{len(users)} <b>Pengguna menggunakan bot ini</b>")


@Bot.on_message(filters.private & filters.command("broadcast") & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        for user in await full_userbase():
            try:
                if query not in [
                    i["message_id"] for i in await message.client.get_messages(user)
                ]:
                    await broadcast_msg.copy(user)
                    successful += 1
                    await asyncio.sleep(3)
                else:
                    deleted += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except BaseException:
                unsuccessful += 1
            total += 1
        await message.reply_text(
            f"Broadcast Selesai\nTotal Pengguna: {total}\n"
            f"Berhasil: {successful}\nGagal: {unsuccessful}\n"
            f"Diblokir: {blocked}\nPesan sudah terkirim: {deleted}"
        )
    else:
        await message.reply_text(
            "Balas pesan yang ingin Anda kirim sebagai broadcast."
        )


@Bot.on_message(filters.private & filters.command("status") & filters.user(ADMINS))
async def get_status(client: Bot, message: Message):
    uptime = await _human_time_duration(time() - client.start_time)
    await message.reply_text(
        text=f"**Bot Uptime:** `{uptime}`\n"
        f"**Userbot Online Sejak:** `{START_TIME_ISO}`"
    )


@Bot.on_message(filters.command("help") & filters.private & subscribed)
async def help_command(client: Bot, message: Message):
    buttons = [
                [
                    InlineKeyboardButton("•ᴄʟᴏsᴇ•", callback_data="close")
                ]
            ]
    await message.reply_text(
        text=f"{client.username} Userbot Help\n\n"
        "Commands:\n"
        "- /start: Memulai Userbot\n"
        "- /broadcast: Mengirim broadcast ke semua pengguna bot\n"
        "- /status: Menampilkan status Userbot\n"
        "- /users: Menampilkan jumlah pengguna bot\n"
        "- /help: Menampilkan pesan bantuan ini\n\n"
        "Note:\n"
        "- Gunakan dengan bijak, jangan spam broadcast\n"
        "- Bot akan menandai pesan broadcast untuk menghindari duplikasi\n"
        "- Dibuat oleh @Mafia_Tobatz\n",
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command("help") & filters.private)
async def not_subscribed(client: Bot, message: Message):
    buttons = [
                [
                    InlineKeyboardButton("•ᴊᴏɪɴ ɴᴏᴡ•", url="https://t.me/CodexBotZ"),
                ]
            ]
    await message.reply_text(
        text="Silakan bergabung dengan saluran untuk menggunakan Userbot ini.\n\n"
        "Bergabung sekarang dan nikmati layanan kami!",
        reply_markup=InlineKeyboardMarkup(buttons),
    )
