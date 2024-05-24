from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["pse", "pause"]) & ~filters.private)
@sudo_users_only
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**𝙎𝙩𝙧𝙚𝙖𝙢 𝙋𝙖𝙪𝙨𝙚𝙙 ☹️**")
        elif a.status == "paused":
            await eor(message, "**𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙋𝙖𝙪𝙨𝙚𝙙 😒**")
        elif a.status == "not_playing":
            await eor(message, "**𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙞𝙨 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 😿**")
    except GroupCallNotFound:
        await eor(message, "**𝙄 𝙖𝙢 𝙉𝙤𝙩 𝙞𝙣 𝙪𝙧 𝙑𝘾 🙄**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["cpse", "cpause"]))
@sudo_users_only
async def pause_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**👉🏻 𝙉𝙤 𝙎𝙩𝙧𝙚𝙖𝙢 𝘾𝙝𝙖𝙩 𝙎𝙚𝙩 ⚡**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**𝙎𝙩𝙧𝙚𝙖𝙢 𝙋𝙖𝙪𝙨𝙚𝙙 ☹️**")
        elif a.status == "paused":
            await eor(message, "**𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙋𝙖𝙪𝙨𝙚𝙙 🙄**")
        elif a.status == "not_playing":
            await eor(message, "**𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙞𝙨 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 😒**")
    except GroupCallNotFound:
        await eor(message, "**𝙄 𝙖𝙢 𝙉𝙤𝙩 𝙞𝙣 𝙑𝘾 😒**")
    except Exception as e:
        print(f"Error: {e}")

  
