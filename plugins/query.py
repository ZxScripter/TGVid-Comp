import os
import time
import asyncio
import sys
import humanize
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import Compress_Stats, skip, CompressVideo
from helper.database import db
from script import Txt


@Client.on_callback_query()
async def Cb_Handle(bot: Client, query: CallbackQuery):
    data = query.data

    if data == 'help':

        btn = [
            [InlineKeyboardButton('ʙᴀᴄᴋ', callback_data='home')]
        ]

        await query.message.edit(text=Txt.HELP_MSG, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)

    if data == 'home':
        btn = [
            [InlineKeyboardButton(text='ʜᴇʟᴘ', callback_data='help'), InlineKeyboardButton(
                text='ᴀʙᴏᴜᴛ', callback_data='about')],
            [InlineKeyboardButton(text='ᴜᴘᴅᴀᴛᴇs', url='https://t.me/Ani_Bots_Updates'), InlineKeyboardButton
                (text='ᴏᴡɴᴇʀ', url='https://t.me/Sensei_Rimuru')]
        ]
        await query.message.edit(text=Txt.PRIVATE_START_MSG.format(query.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))

    elif data == 'about':
        BUTN = [
            [InlineKeyboardButton(text='ʙᴀᴄᴋ', callback_data='home')]
        ]
        botuser = await bot.get_me()
        await query.message.edit(Txt.ABOUT_TXT.format(botuser.username), reply_markup=InlineKeyboardMarkup(BUTN), disable_web_page_preview=True)

    if data.startswith('stats'):

        user_id = data.split('-')[1]

        try:
            await Compress_Stats(e=query, userid=user_id)

        except Exception as e:
            print(e)

    elif data.startswith('skip'):

        user_id = data.split('-')[1]

        try:

            await skip(e=query, userid=user_id)
        except Exception as e:
            print(e)

    elif data == 'option':
        file = getattr(query.message.reply_to_message,
                       query.message.reply_to_message.media.value)

        text = f"""**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ ?**\n\n**ғɪʟᴇ ɴᴀᴍᴇ ** :- `{file.file_name}`\n\n**ғɪʟᴇ sɪᴢᴇ** :- `{humanize.naturalsize(file.file_size)}`"""
        buttons = [[InlineKeyboardButton("ʀᴇɴᴀᴍᴇ 📝", callback_data=f"rename-{query.from_user.id}")],
                   [InlineKeyboardButton("ᴄᴏᴍᴘʀᴇss ⚡", callback_data=f"compress-{query.from_user.id}")]]

        await query.message.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons))

    elif data == 'setffmpeg':
        try:
            ffmpeg_code = await bot.ask(text=Txt.SEND_FFMPEG_CODE, chat_id=query.from_user.id, filters=filters.text, timeout=60, disable_web_page_preview=True)
        except:
            return await query.message.reply_text("**Eʀʀᴏʀ!!**\n\nRᴇǫᴜᴇsᴛ ᴛɪᴍᴇᴅ ᴏᴜᴛ.\nSᴇᴛ ʙʏ ᴜsɪɴɢ /set_ffmpeg")

        SnowDev = await query.message.reply_text(text="**sᴇᴛᴛɪɴɢ ʏᴏᴜʀ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ**...")
        await db.set_ffmpegcode(query.from_user.id, ffmpeg_code.text)
        await SnowDev.edit("✅️ **ғғᴍᴘᴇɢ ᴄᴏᴅᴇ sᴇᴛ sᴜᴄᴄᴇssғᴜʟʟʏ**")


    elif data.startswith('compress'):
        user_id = data.split('-')[1]

        if int(user_id) not in [query.from_user.id, 0]:
            return await query.answer(f"⚠️ Hᴇʏ {query.from_user.first_name}\nTʜɪs ɪs ɴᴏᴛ ʏᴏᴜʀ ғɪʟᴇ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴀɴʏ ᴏᴘᴇʀᴀᴛɪᴏɴ", show_alert=True)

        else:

            BTNS = [
                [InlineKeyboardButton(text='480p', callback_data='480pc'), InlineKeyboardButton(
                    text='720p', callback_data='720pc')],
                [InlineKeyboardButton(text='1080p', callback_data='1080pc'), InlineKeyboardButton(
                    text='4K', callback_data='2160pc')],
                [InlineKeyboardButton(
                    text='ᴄᴜsᴛᴏᴍ ᴇɴᴄᴏᴅɪɴɢ ⚡', callback_data='custompc')],
                [InlineKeyboardButton(text='ᴄʟᴏsᴇ', callback_data='close'), InlineKeyboardButton(
                    text='ʙᴀᴄᴋ', callback_data='option')]
            ]
            await query.message.edit(text='**sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄᴏᴍᴘʀᴇssɪᴏɴ ᴍᴇᴛʜᴏᴅ ʙᴇʟᴏᴡ 👇 **', reply_markup=InlineKeyboardMarkup(BTNS))

    elif data == '480pc':
        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg = "-preset veryfast -c:v libx264 -s 854x480 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 28 -c:a libopus -b:a 40k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5"
            await CompressVideo(bot=bot, query=query, ffmpegcode=ffmpeg, c_thumb=c_thumb)

        except Exception as e:
            print(e)

    elif data == '720pc':
        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg = "-preset veryfast -c:v libx264 -s 1280x720 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 26 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5"
            await CompressVideo(bot=bot, query=query, ffmpegcode=ffmpeg, c_thumb=c_thumb)

        except Exception as e:
            print(e)

    elif data == '1080pc':

        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg = "-preset veryfast -c:v libx264 -s 1920x1080 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 24 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5"
            await CompressVideo(bot=bot, query=query, ffmpegcode=ffmpeg, c_thumb=c_thumb)

        except Exception as e:
            print(e)

    elif data == '2160pc':

        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg = "-preset veryfast -c:v libx264 -s 3840x2160 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 21 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 5"
            await CompressVideo(bot=bot, query=query, ffmpegcode=ffmpeg, c_thumb=c_thumb)

        except Exception as e:
            print(e)

    elif data == 'custompc':

        try:
            c_thumb = await db.get_thumbnail(query.from_user.id)
            ffmpeg_code = await db.get_ffmpegcode(query.from_user.id)

            if ffmpeg_code:
                await CompressVideo(bot=bot, query=query, ffmpegcode=ffmpeg_code, c_thumb=c_thumb)

            else:
                BUTT = [
                    [InlineKeyboardButton(
                        text='sᴇᴛ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ', callback_data='setffmpeg')],
                    [InlineKeyboardButton(
                        text='ʙᴀᴄᴋ', callback_data=f'compress-{query.from_user.id}')]
                ]
                await query.message.edit(text="ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ.", reply_markup=InlineKeyboardMarkup(BUTT))
        except Exception as e:
            print(e)

    elif data.startswith("close"):

        user_id = data.split('-')[1]
        
        if int(user_id) not in [query.from_user.id, 0]:
            return await query.answer(f"⚠️ Hᴇʏ {query.from_user.first_name}\nTʜɪs ɪs ɴᴏᴛ ʏᴏᴜʀ ғɪʟᴇ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴏ ᴀɴʏ ᴏᴘᴇʀᴀᴛɪᴏɴ", show_alert=True)
        
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
