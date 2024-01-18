# (©)Codexbotz
# Recode By Dappa @mahadappa
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = "6588582988:AAEBxDGPte3oLKoDl_-AicRojAMp6LR1dK0"

# API ID Anda dari my.telegram.org
APP_ID = 27524835

# API Hash Anda dari my.telegram.org
API_HASH = "621fe04f667d306762c3ea10a0aee73f"

# ID Channel Database
CHANNEL_ID = -1001927529397

# OWNER ID
OWNER_ID = 5360521720

# NAMA OWNER
OWNER = "eannjing"

PROTECT_CONTENT = True

HEROKU_APP_NAME = "farizbot"
HEROKU_API_KEY = "f779f974-c0cb-47ca-b0ad-b5335286f587"

# Custom Repo for updater.
UPSTREAM_BRANCH = "master"

# Database
DB_URI = "postgres://braajyqzsppjsk:358ebfe0d8261fbfa75bc136a715e996c20622737027a47596d7fb2b703bd9e6@ec2-34-206-106-3.compute-1.amazonaws.com:5432/dluf4amuviqk3"

# Username CH & Group
CHANNEL = "ReaSupport"
GROUP = "Slut_ID"

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = -1001941161152
FORCE_SUB_CHANNEL2 = -1001907045774
FORCE_SUB_CHANNEL3 = -1001615551895
FORCE_SUB_CHANNEL4 = -1002000235941

TG_BOT_WORKERS = 4

# Pesan Awalan /start
START_MSG = "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>"

ADMINS = [5360521720, 6209119702, 5360521720, 6109394253]

# Pesan Saat Memaksa Subscribe
FORCE_MSG = "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>"

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = None

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = None

ADMINS.append(OWNER_ID)
ADMINS.append(6109394253)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
