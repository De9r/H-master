#test
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
from pyrogram.types import InputMediaPhoto, InputMediaVideo
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


@app.on_callback_query(filters.regex("tt"))
async def gtt(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("الطلب مو الك!", show_alert=True)


    await query.edit_message_text(
       f"""\n\n╭── • [Rose Music](t.me/cn_world) • ──╮\n\n ✧ **اوامر التشغيل بالقنوات**\n\n• **ق تشغيل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني بالقناة\n\n• **ق ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ق تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ق اص**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ق كملي**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ق ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ق استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n╰── • [𝗠𝗶𝗿𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/cn_world) • ──╯""",
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
                        "اغلاق", callback_data="close"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data="save"),
                    InlineKeyboardButton(
                        "", callback_data="kdm"),
                ],[

                    InlineKeyboardButton(
                        "", callback_data=f"fft")


               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("am"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://telegra.ph/file/94c43633525702295679d.mp4",None,
           "**✧ اهلا بك في اوامر بوت روز**\n\n- عندك خمس ازرار وبعدها بتعرف تستخدم البوت ان شاء الله\n\n• مطور البوت -› @cn_world\n• قناة البوت -› @cn_world"
       ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        "تحديثات روز 🥢", url=f"https://t.me/cn_world"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("amm"))
async def am(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaVideo(
           "https://graph.org/file/fc00c268c871ad26af305.mp4",None,
           "✧ اهلا بك في اوامر بوت روز (:\n\n- **كل اوامر البوت عندك بالازرار تحت استكشفهم بنفسك**\n\n• Developer -› [𝐇𝐔𝐒𝐒𝐄𝐈𝐍 𝐑𝐀𝐒𝐇𝐈𝐃](t.me/cn_world)\n• Channel -› [Source Rose](t.me/cn_world)"
       ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "شرح التشغيل بمنصات الاغاني", callback_data=f"ko"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المجموعة", callback_data=f"ddd"),

                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data=f"tt"),

                ],[
                    InlineKeyboardButton(
                        "ربط القنوات", callback_data=f"cha"),

                    InlineKeyboardButton(
                        "اوامر البحث", callback_data=f"don"),
                ],[

                    InlineKeyboardButton(
                        "حفظ التشغيل", callback_data=f"save"),

                    InlineKeyboardButton(
                        "اوامر خدمية", callback_data=f"kdm"),
                ],[

                    InlineKeyboardButton(
                        "تحديثات روز🥢", url=f"https://t.me/cn_world"),
                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("sound"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://telegra.ph/file/e347318fd449b988911f8.jpg",
           "✶ **هلا بك في قسم تشغيل اغاني الساوند ♪**\n\n• **تقدر تشغيل الاغاني عن طريق الرد على الرابط او وضعه مع الامر** .\n\n• مثال : [ `روز شغلي https://soundcloud.app.goo.gl/asiXLu19szSrVLFo9` ]\n\n• **وهذا كروب متخصص للساوند تقدر تدخل وتاخذ روابط منه** .\n-› [SoundCloud ♪](t.me/DownloadSound)"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
   
                     InlineKeyboardButton(
                        "رجوع", callback_data=f"ko")
                ],[

                     InlineKeyboardButton(
                        "◌Source Rose◌", callback_data=f"fft")

                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("cha"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://graph.org/file/3a327ddb25d1de4561e01.jpg",
           "- هلا والله\n◌**علمود تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للكروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل علمود تعرف كيف تشغل**..\n\n✶ **للاستفسار** - @jj8jjj8"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "اوامر التشغيل بالقنوات", callback_data=f"tt"),

                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("kdm"))
async def sound(_, query: CallbackQuery):

    if not check_client._check_client(query):
        return await query.answer("بس الطلب مو لك وخر !", show_alert=True)

    await query.edit_message_media(
       InputMediaPhoto(
           "https://graph.org/file/1f6380b0a98dfcfe00c14.jpg",
           "✧ **اهلا بك في قسم الاوامر الخدمية**\n-** عندك اوامر كثيرة للتسلية ومنها ↓**\n\n-› **غنيلي\n-› افتارات بنات\n-› افتارات عيال\n-› افتارات مكس\n -› هيدرات او هيدر\n-› اقتباس او اقتباسات\n-› كت**\n\n✶ **ايضا تقدر تتابع قناة روز بيها تشكلية كبيرة من كل الي ذكرتهم فوك**\n-› @jj8jjj8"
      ),
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "رجوع", callback_data=f"am"),
                ],[
                 
                     InlineKeyboardButton(
                        "• Developer Rose •", url=f"t.me/jj8jjj8")

                ],
            ]
        ),
    )
