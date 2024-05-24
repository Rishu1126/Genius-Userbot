from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import NoActiveGroupCall


@app.on_message(cdx(["join", "joinvc"]) & ~filters.private)
@sudo_users_only
async def join_vc(client, message):
    chat_id = message.chat.id
    a_calls = await call.calls
    if_chat = a_calls.get(chat_id)
    if if_chat:
        return await eor(
            message, "**𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙅𝙤𝙞𝙣𝙚𝙙 𝙑𝘾!**"
        )
    if not if_chat:
        try:
            await call.play(chat_id)
            return await eor(
                message, "**𝙅𝙤𝙞𝙣𝙚𝙙 𝙑𝘾!**"
            )
        except NoActiveGroupCall:
            return await eor(
                message, "**𝙉𝙤 𝘼𝙘𝙩𝙞𝙫𝙚 𝙑𝙘 𝙁𝙤𝙪𝙣𝙙!**"
            )
        except Exception as e:
            print(f"Error: {e}")
            pass
        


@app.on_message(cdz(["cjoin", "cjoinvc"]))
@sudo_users_only
async def join_vc_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**👉🏻 𝙉𝙤 𝙎𝙩𝙧𝙚𝙖𝙢 𝘾𝙝𝙖𝙩 𝙎𝙚𝙩 😒**"
    )
    a_calls = await call.calls
    if_chat = a_calls.get(chat_id)
    if if_chat:
        return await eor(
            message, "**𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙅𝙤𝙞𝙣𝙚𝙙 𝙑𝘾!**"
        )
    if not if_chat:
        try:
            await call.play(chat_id)
            return await eor(
                message, "**𝙅𝙤𝙞𝙣𝙚𝙙 𝙑𝘾!**"
            )
        except NoActiveGroupCall:
            return await eor(
                message, "**𝙉𝙤 𝘼𝙘𝙩𝙞𝙫𝙚 𝙑𝘾!**"
            )
        except Exception as e:
            print(f"Error: {e}")
            pass
