import asyncio
import shutil
import humanize
from time import sleep
from config import Config
from script import Txt
from helper.database import db
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from .check_user_status import handle_user_status
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message((filters.private | filters.group))
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)

@Client.on_message((filters.private | filters.group) & filters.command('start'))
async def Handle_StartMsg(bot:Client, msg:Message):

    Snowdev = await msg.reply_text(text= '**Please Wait...**', reply_to_message_id=msg.id)

    if msg.chat.type == enums.ChatType.SUPERGROUP and not await db.is_user_exist(msg.from_user.id):
        botusername = await bot.get_me()
        btn = [
            [InlineKeyboardButton(text='ʙᴏᴛ ᴘᴍ', url=f'https://t.me/{botusername.username}')],
            [InlineKeyboardButton(text='ᴏᴡɴᴇʀ', url='https://t.me/Sensei_Rimuru')]
        ]

        await Snowdev.edit(text=Txt.GROUP_START_MSG.format(msg.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))
    
    else:
        btn = [
            [InlineKeyboardButton(text='ʜᴇʟᴘ', callback_data='help'), InlineKeyboardButton(text='ᴀʙᴏᴜᴛ', callback_data='about')],
            [InlineKeyboardButton(text='ᴜᴘᴅᴀᴛᴇs', url='https://t.me/Ani_Bots_Updates'), InlineKeyboardButton(text='ᴏᴡɴᴇʀ', url='https://t.me/Sensei_Rimuri')]
        ]

        if Config.START_PIC:
            await Snowdev.delete()
            await msg.reply_photo(photo=Config.START_PIC, caption=Txt.PRIVATE_START_MSG.format(msg.from_user.mention), reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=msg.id)
        else:
            await Snowdev.delete()
            await msg.reply_text(text=Txt.PRIVATE_START_MSG.format(msg.from_user.mention), reply_markup=InlineKeyboardMarkup(btn), reply_to_message_id=msg.id)
            
    

@Client.on_message((filters.private | filters.group) & (filters.document | filters.audio | filters.video))
async def Files_Option(bot:Client, message:Message):
    
    SnowDev = await message.reply_text(text='**Please Wait**', reply_to_message_id=message.id)

    if message.chat.type == enums.ChatType.SUPERGROUP and not await db.is_user_exist(message.from_user.id):
        botusername = await bot.get_me()
        btn = [
            [InlineKeyboardButton(text='ʙᴏᴛ ᴘᴍ', url=f'https://t.me/{botusername.username}')],
            [InlineKeyboardButton(text='ᴏᴡɴᴇʀ', url='https://t.me/Sensei_Rimuru')]
        ]

        return await SnowDev.edit(text=Txt.GROUP_START_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(btn))
        
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)


    try:
        text = f"""**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.?**\n\n**ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ғɪʟᴇ sɪᴢᴇ** :- `{filesize}`"""

        buttons = [[InlineKeyboardButton("ʀᴇɴᴀᴍᴇ 📝", callback_data=f"rename-{message.from_user.id}")],
                   [InlineKeyboardButton("ᴄᴏᴍᴘʀᴇss ⚡", callback_data=f"compress-{message.from_user.id}")]]
        await SnowDev.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        
    except FloodWait as e:
        
        floodmsg = await message.reply_text(f"**😥 ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴅᴏɴ'ᴛ sᴘᴀᴍ ғᴏʀ ᴀɴᴏᴛʜᴇʀ {e.value} Sᴇᴄᴄᴏɴᴅs**", reply_to_message_id=message.id)
        await sleep(e.value)
        await floodmsg.delete()

        text = f"""**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.?**\n\n**ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ғɪʟᴇ sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[InlineKeyboardButton("ʀᴇɴᴀᴍᴇ 📝", callback_data=f"rename-{message.from_user.id}")],
                   [InlineKeyboardButton("ᴄᴏᴍᴘʀᴇss ⚡", callback_data=f"compress-{message.from_user.id}")]]
        await SnowDev.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons))

    except Exception as e:
        print(e)

@Client.on_message((filters.private | filters.group) & filters.command('cancel'))
async def cancel_process(bot:Client, message:Message):
    
    try:
        shutil.rmtree(f"encode/{message.from_user.id}")
        shutil.rmtree(f"ffmpeg/{message.from_user.id}")
        shutil.rmtree(f"Renames/{message.from_user.id}")
        shutil.rmtree(f"Metadata/{message.from_user.id}")
        shutil.rmtree(f"Screenshot_Generation/{message.from_user.id}")
        
        return await message.reply_text(text="**ᴄᴀɴᴄᴇʟʟᴇᴅ ᴀʟʟ ᴏɴɢᴏɪɴɢ ᴘʀᴏᴄᴇss ✅**")
    except BaseException:
        pass
