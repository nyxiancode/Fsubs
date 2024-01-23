import asyncio
import base64
import re
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from config import ADMINS, FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP_2


async def subschannel(client, update):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL_2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL, user_id=user_id
        )
        member2 = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_2, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return (
        member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
        or member2.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
    )


async def subsgroup(client, update):
    if not FORCE_SUB_GROUP and not FORCE_SUB_GROUP_2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB_GROUP, user_id=user_id)
        member2 = await client.get_chat_member(chat_id=FORCE_SUB_GROUP_2, user_id=user_id)
    except UserNotParticipant:
        return False

    return (
        member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
        or member2.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
    )


async def subschannel2(client, update):
    if not FORCE_SUB_CHANNEL_2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member2 = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL_2, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member2.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def subsgroup2(client, update):
    if not FORCE_SUB_GROUP_2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member2 = await client.get_chat_member(chat_id=FORCE_SUB_GROUP_2, user_id=user_id)
    except UserNotParticipant:
        return False

    return member2.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]


async def is_subscribed(client, update):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL_2:
        return True
    if not FORCE_SUB_GROUP and not FORCE_SUB_GROUP_2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB_GROUP, user_id=user_id)
        member2 = await client.get_chat_member(chat_id=FORCE_SUB_CHANNEL_2, user_id=user_id)
    except UserNotParticipant:
        return False
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL, user_id=user_id
        )
        member2 = await client.get_chat_member(chat_id=FORCE_SUB_GROUP_2, user_id=user_id)
    except UserNotParticipant:
        return False

    return (
        member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
        or member2.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]
    )

# Sisanya tetap sama...
