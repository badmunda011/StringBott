from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʏ {msg.from_user.mention}🍷,

ɪ ᴀᴍ ᴛʀᴜꜱᴛᴇᴅ ꜱᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ꜰᴜʟʟʏ ꜱᴀꜰᴇ & ꜱᴇᴄᴜʀᴇ.
ɴᴏ ᴇʀʀᴏʀ.

‌🇲‌ᴀᴅᴇ ʙʏ  : [⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸](https://t.me/ll_BAD_MUNDA_ll) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🌹ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ🌹", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🥀ɢʀᴏᴜᴘ🥀", url="https://t.me/PUNJABI_CHATTING_HUB"),
                    InlineKeyboardButton("☠️ᴄʜᴀɴɴᴇʟ☠️", url="https://t.me/PBX_PERMOT")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
