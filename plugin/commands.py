"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  Zaute Km | TGVCSETS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES, mp
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>𝐇𝐚𝐲 𝐒𝐥𝐮𝐫𝐫𝐫, [{}](tg://user?id={})\n\nI 𝐬𝐚𝐲𝐚 𝐛𝐢𝐬𝐚 𝐦𝐞𝐦𝐮𝐭𝐚𝐫𝐤𝐚𝐧 𝐚𝐧𝐝𝐚 𝐥𝐚𝐠𝐨 𝐚𝐭𝐚𝐨 𝐫𝐚𝐝𝐢𝐨 𝐥𝐢𝐯𝐞 𝐧𝐨𝐧 𝐬𝐭𝐨𝐩!.\n\n𝐤𝐞𝐭𝐢𝐤 /𝐡𝐞𝐥𝐩 𝐣𝐢𝐤𝐚 𝐦𝐞𝐦𝐛𝐮𝐭𝐮𝐡𝐤𝐚𝐧 𝐛𝐚𝐧𝐭𝐮𝐚𝐧
𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 ☕ 𝐛𝐲 @LordGanss10 𝐇𝐮𝐛𝐮𝐧𝐠𝐢 𝐎𝐰𝐧𝐞𝐫 𝐒𝐚𝐲𝐚 𝐉𝐢𝐤𝐚 𝐈𝐧𝐠𝐢𝐧 𝐚𝐝𝐚 𝐘𝐠 𝐃𝐢𝐭𝐚𝐧𝐲𝐚𝐤𝐚𝐧 𝐀𝐭𝐚𝐮 𝐂𝐚𝐫𝐚 𝐂𝐚𝐫𝐚 𝐌𝐞𝐦𝐛𝐮𝐚𝐭 𝐁𝐨𝐭 𝐌𝐮𝐬𝐢𝐜 𝐃𝐥𝐥</b>"
HELP = """
**User Commands:**
▷/play **[song name]/[yt link]**: Reply to an audio file.
▷/dplay **[song name]:** Play music from Deezer.
▷/player:  Show current playing song.
▷/help: Show help for commands.
▷/playlist: Shows the playlist.

**Admin Commands:**
▷/skip **[n]** ...  Skip current or n where n >= 2
▷/join: Join voice chat.
▷/leave: Leave current voice chat
▷/vc: Check which VC is joined.
▷/stop: Stop playing.
▷/radio: Start Radio.
▷/stopradio: Stops Radio Stream.
▷/replay: Play from the beginning.
▷/clean: Remove unused RAW PCM files.
▷/pause: Pause playing.
▷/resume: Resume playing.
▷/mute: Mute in VC.
▷/unmute: Unmute in VC.
▷/restart: Restarts the Bot.
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("🔥 𝐎𝐰𝐧𝐞𝐫 🔥", url='https://github.com/LushaiMusic/VCMusicPlayer'),
    ],
    [
        InlineKeyboardButton('👥 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/bacotsi/5'),
        InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥 📢', url='https://t.me/anjay/6'),
    ],
    [
        InlineKeyboardButton('🆘 𝐇𝐞𝐥𝐩 & 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 🆘', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🔥 𝐎𝐰𝐧𝐞𝐫 🔥", url='https://t.me/LordGanss10'),
        ],
        [
            InlineKeyboardButton('👥 𝐆𝐫𝐨𝐮𝐩', url='https://t.me/bacotsi/5'),
            InlineKeyboardButton('𝐂𝐡𝐚𝐧𝐧𝐞𝐥 📢', url='https://t.me/anjay/6'),
        ],
        [
            InlineKeyboardButton('𝐎𝐰𝐧𝐞𝐫', url='https://t.me/LordGanss10'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("🔄 Restarting...")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        process.send_signal(signal.SIGTERM) 
    os.execl(sys.executable, sys.executable, *sys.argv)
    
