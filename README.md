# Fsub

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus.

<img src="https://kutmut.my.id/logop.png">


### Setup Repo ini join 4 ch ngentod

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel ForceSub tambahkan bot sebagai ADMIN
- Tambahkan bot ke Group ForceSub tambahkan bot sebagai ADMIN

##
### Installation

### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://kutmut.my.id/deploy)</br>




#### Deploy in your VPS
````bash
git clone https://github.com/altercodes/Fsubs
````
````bash
cd Fsubs
````
````bash
pip3 install -r requirements.txt
````
```create config.py appropriately```
````bash
python3 main.py
````

### Admin Commands

```
/start - mulai bot atau dapatkan postingan

/batch - buat link untuk lebih dari satu posting

/genlink - buat link untuk satu posting

/users - lihat statistik pengguna bot

/broadcast - menyiarkan/broadcast pesan apa pun ke pengguna bot

/ping - untuk mengecek bot
```

### Variables

* `API_HASH` Dapatkan API HASH di web my.telegram.org.
* `API_ID` Dapatkan APP ID di web my.telegram.org
* `TG_BOT_TOKEN` Dapatkan dari t.me/BotFather
* `OWNER` Masukan Username Telegram untuk Owner BOT
* `OWNER_ID` Masukan User ID Telegram untuk Owner BOT
* `CHANNEL_ID` Masukan ID Channel Untuk [Channel Database] contoh:- -100xxxxxxxx
* `ADMINS` Masukan User ID untuk mendapatkan hak Admin BOT [Hanya dapat membuat link]
* `START_MESSAGE` Opsional: Pesan /start memulai awalan ke bot, Gunakan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> parsemode HTML 
* `FORCE_SUB_MESSAGE` Opsional: Pesan Paksa Subscribe bot, Gunakan Format parsemode HTML
* `FORCE_SUB1` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB2` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB3` Masukan ID dari Channel Untuk Wajib Subscribenya
* `FORCE_SUB4` Masukan ID dari Channel Untuk Wajib Subscribenya
### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Bergabunglah di [Group Telegram ](https://www.telegram.dog/slut_id) Untuk Dukungan/Bantuan [Kyu](https://www.telegram.dog/sayakyu) untu info Update bot.   
   
Laporkan Bug, Berikan Permintaan Fitur Di sana.. 

### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Thanks To [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot)
- Our Support Group Members

