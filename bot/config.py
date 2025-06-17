import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID", "20928172"))
    API_HASH = os.environ.get("API_HASH", "48ed56c8db54f85d232f576b150360ef")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "skpk05122")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://skpk05122:LTKtHfA3oD24aHXk@cluster0.oe7misv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    OWNER_ID = int(os.environ.get("OWNER_ID", "6443740402"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002556958706"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "False"), False)
    WEBHOOK = True  # Don't change this
    PORT = int(os.environ.get("PORT", 8000))
    THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "https://te.legra.ph/file/159d3f9e2d57dd02db970.jpg").split()))

    # Constants
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):
    START_MESSAGE = (
        " {mention}\n\nsᴇɴᴅ ᴀɴʏ ʟɪɴᴋ ᴏʀ ᴛxᴛ ғɪʟᴇ."
    )
    DEV_MESSAGE = """👋 Hey there, I'm [‎ ‎ִֶָ‎ִֶָ𓂃 ࣪˖ ִֶָ𝐒ɦε ۶ৎ !!](https://t.me/rajcontactbot)) – your go-to Telegram bot developer!

🤖 Love having bots that do the heavy lifting for you? That's my jam! I'm all about crafting super cool and custom Telegram bots that make your life a breeze.

✨ **What I Do**

- **Bot Magic:** From automating tasks to interactive games, I create bots that do it all. Seriously, ask me anything!
- **Tailored to You:** Your bot, your rules. I'll whip up a bot that's as unique as you are.
- **Chill Vibes:** I keep your data super safe, so you can relax and enjoy the bot party.
- **Always Improving:** Telegram evolves, and my bots grow with it. I'm here to keep things fresh and fab.

Ready for your own bot buddy? Ping me on [Telegram](https://t.me/1234) or check out me on [GitHub](https://github.com/1234). Wanna hire me?

Let's bot up and have some fun! 🤘"""
    HELP_MESSAGE = os.environ.get("HELP_MESSAGE", "Help message")
    PROGRESS_MESSAGE = """**╔════❰ Uploading ❱══❍
║╭━➣
║┣⪼  Progress:-  {percentage}%
║┣ 
║┣⪼ {progress}
║┣
║┣⪼《{finished} of {total}》
║┣ 
║┣⪼ Speed:- {speed}/s
║┣ 
║┣⪼ ETA:- {eta} 
║╰━➣
╚════════════════❍**"""
    NEW_USER_MESSAGE = """#NewUser

🆔 User ID: `{user_id}`
👤 User: {mention}
"""
    DOWNLOADING = """📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥 
    
📟 {start_index}/{end_index}

📝 Name » {link_no} » {name}

🔢Index: {orginal_start_index}/{orginal_end_index}

...sᴀɪɴɪ ʙᴏᴛs..."""

    DEFAULT_CAPTION = """[📁] File_ID : {file_index}

𖤓 𝐓ɪᴛʟᴇ  : {file_name}

🗃 𝐒𝐢𝐳𝐞 : {file_size}

📚 Bᴀᴛᴄʜ Nᴀᴍᴇ : {batch_name}

🌟 Exᴛʀᴀᴄᴛᴇᴅ Bʏ : [‎ ‎ִֶָ‎ִֶָ𓂃 ࣪˖ ִֶָ𝐒ɦε ۶ৎ !!‌](https://t.me/rajcontactbot)"""


    CAPTION_CB = """**Set Caption

➢ Available Variables 👇**

┌🎴 𝐍𝐚𝐦𝐞 : `{file_name}`
├🗃 𝐒𝐢𝐳𝐞 : `{file_size}`
├⚙️ 𝐄𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧 : `{file_extension}`
├🧭 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 : `{file_duration}`
├🖇 𝐋𝐢𝐧𝐤 : `{file_url}`
├🔢 𝐈𝐧𝐝𝐞𝐱 : `{file_index}`
├🗳 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞 : `{batch_name}`

==============================

➢ Current:
`{current_caption}`

==============================

➢ **Default:**
`{default_caption}`

➢ **Status:** {status}"""
