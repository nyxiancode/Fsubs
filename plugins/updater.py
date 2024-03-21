import os
import sys
import subprocess
from os import environ, execle
from bot import Bot
from git import Repo
from git.exc import InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS, LOGGER

UPSTREAM_REPO = "https://github.com/alteregocodes/4tombol"


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"<b>perbaruan untuk <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"perbaruan untuk {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"main..upstream/{ac_br}")
    return bool(changelog)


@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_bot(_, message: Message):
    message.chat.id
    msg = await message.reply_text("Memeriksa pembaruan...")
    try:
        update_avail = updater()
        if update_avail:
            await msg.edit("✅ Pembaruan selesai!")
            subprocess.run(["git", "pull", "-f"])
            subprocess.run(["pip3", "install", "--no-cache-dir", "-r", "requirements.txt"])
            execle(sys.executable, sys.executable, "main.py", environ)
            return
    except Exception as e:
        await msg.edit(f"❌ Pembaruan gagal: {str(e)}")
        return

    await msg.edit(
        f"Bot sudah diperbarui dari @AlteregoNetwork ^^)",
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("`Merestart bot...`")
        LOGGER(__name__).info("SERVER BOT DIRESTART !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot telah direstart!\n\n")
    os.system(f"kill -9 {os.getpid()} && bash start")
