import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

from YukkiMusic import check_client


@app.on_callback_query(filters.regex("ddd"))
async def dddf(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer(" بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""\n\n\n╭── • [ROSR MUSIC](t.me/cn_world) • ──╮\n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **ميرا شغلي + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **ميرا طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ميرا الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ميرا اص** او **اسكتي**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ميرا تكلمي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ميرا ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ميرا كملي** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/NvvvC) • ──╯""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/cn_world")
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="am"),
                    InlineKeyboardButton(
                        "", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ rose", callback_data="fft"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )

@app.on_callback_query(filters.regex("sop"))
async def sop(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("بس الطلب مو لك !!", show_alert=True)

    await query.edit_message_text(
       f"""✧ اهلا بك في سورس روز \n✧ قناة السورس @cn_world \n✧ اي مشكلة تواجهك تواصل معي @jj8jjj8""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/cn_world")
                ],[
                    InlineKeyboardButton(
                        "◌ Source Rose ◌", callback_data="am"),
                    InlineKeyboardButton(
                        "◌ Developer ◌", url=f"t.me/jj8jjj8")
                ],[

                    InlineKeyboardButton(
                        "رجوع", callback_data="settings_helper"),
                    InlineKeyboardButton(
                        "", callback_data="am"),

               ],
          ]
        ),
    )
