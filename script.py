class Txt(object):

    PRIVATE_START_MSG = """
ʜɪɪ {},

**ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʀᴇɴᴀᴍᴇʀ + ᴄᴏᴍᴘʀᴇssᴏʀ ʙᴏᴛ. ‼️ ᴇxᴘʟᴏʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ "⚡ ʜᴇʟᴘ ⚡" ʙᴜᴛᴛᴏɴ ᴛᴏ ᴜsᴇ ᴍᴇ ᴍᴏʀᴇ ᴘʀᴇᴄɪsᴇʟʏ**
"""
    GROUP_START_MSG = """
Hɪ {},

**ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʀᴇɴᴀᴍᴇʀ + ᴄᴏᴍᴘʀᴇssᴏʀ ʙᴏᴛ**

**‼️ ᴇxᴘʟᴏʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ "⚡ ʜᴇʟᴘ ⚡" ʙᴜᴛᴛᴏɴ ᴛᴏ ᴜsᴇ ᴍᴇ ᴍᴏʀᴇ ᴘʀᴇᴄɪsᴇʟʏ**
"""
    PROGRESS_BAR = """<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣‣ 💾 sɪᴢᴇ: {1} | {2}
┣‣ ♻️ ᴘʀᴏɢʀᴇss : {0}%
┣‣ ⚡ sᴘᴇᴇᴅ: {3}/s
┣‣ 🕛 ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━➣ </b>"""

    SEND_FFMPEG_CODE = """
❪ SET CUSTOM FFMPEG CODE ❫

‣ **ʜᴏᴡ ᴛᴏ sᴇᴛ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ**

‣ ffmpeg -i input.mkv <code> -c:v libx264 -crf 24 </code> output.mkv

<code> -c:v libx264 -crf 24 </code> **ᴛʜɪs ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ.**

• **ғᴏʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ - @Sensei_Rimuru**
"""

    SEND_METADATA ="""
❪ SET CUSTOM METADATA ❫

‣ **ғᴏʀ ᴇxᴀᴍᴘʟᴇ** -

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Encoded By Anime Sensei" -metadata author="Anime Sensei" -metadata:s:s title="Anime Sensei" -metadata:s:a title="Anime Sensei" -metadata:s:v title="Anime Sensei" </code>

• **ғᴏʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ - @Sensei_Rimuru**
"""

    
    HELP_MSG = """
‣ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs -

‣ /set_ffmpeg - To set custom ffmpeg code
‣ /set_metadata - To set custom metadata code
‣ /set_caption - To set custom caption
‣ /del_ffmpeg - Delete the custom ffmpeg code
‣ /del_caption - Delete caption
‣ /see_ffmpeg - View custom ffmpeg code
‣ /see_metadata - View custom metadata code
‣ /see_caption - View caption 
‣ To Set Thumbnail just send photo


<b>ᴏᴡɴᴇʀ</b> <a href=https://t.me/Anime_Sensei_Network>Anime Sensei</a>
"""

    ABOUT_TXT = """<b>╭───────────⍟
├ᴍy ɴᴀᴍᴇ : @{}
├Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>
╰───────────────⍟ """
