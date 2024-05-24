from ... import *
from pyrogram import filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat


async def get_vc_call(client, message):
    chat_id = message.chat.id
    chat_peer = await client.resolve_peer(chat_id)
    if isinstance(chat_peer,
        (InputPeerChannel, InputPeerChat)
    ):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(
                    GetFullChannel(channel=chat_peer)
                )
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(
                    GetFullChat(chat_id=chat_peer.chat_id)
                )
            ).full_chat
            
        if full_chat is not None:
            return full_chat.call
            
    return False

@app.on_message(cdx(["svc", "startvc"]) & ~filters.private)
@sudo_users_only
async def create_video_chat(client, message):
    chat_id = message.chat.id
    try:
        aux = await eor(message, "**🔄 𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜 ...**")
        vc_call = await get_vc_call(client, message)
        if vc_call:
            return await aux.edit("**👉🏻 𝙑𝘾 𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝘼𝙘𝙩𝙞𝙫𝙚❗**")
        peer = await client.resolve_peer(chat_id)
        await client.invoke(
            CreateGroupCall(
                peer=peer,
                random_id=client.rnd_id() // 9000000000,
            ),
        )
        await aux.edit("**👉🏻 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙑𝘾. 🌿**")
    except Exception as e:
        print(f"Error: {e}")
        pass



@app.on_message(cdx(["dvc", "evc", "stopvc", "endvc"]) & ~filters.private)
@sudo_users_only
async def discard_video_chat(client, message):
    user_id = message.from_user.id
    try:
        aux = await eor(message, "**🔄 𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜 ...**")
        vc_call = await get_vc_call(client, message)
        if not vc_call:
            return await aux.edit("**👉🏻 𝙑𝘾 𝙉𝙤𝙩 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙔𝙚𝙩❗**")
        await client.invoke(
            DiscardGroupCall(call=vc_call)
        )
        return await aux.edit("**👉🏻 𝙎𝙪𝙘𝙘𝙚𝙨𝙛𝙪𝙡𝙡𝙮 𝙀𝙣𝙙𝙚𝙙 𝙑𝘾. 🌿**")
    except Exception as e:
        print(f"Error: {e}")
        pass


@app.on_message(cdx(["rvc", "restartvc"]) & ~filters.private)
@sudo_users_only
async def discard_video_chat(client, message):
    chat_id = message.chat.id
    try:
        aux = await eor(message, "**🔄 𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜 ...**")
        vc_call = await get_vc_call(client, message)
        if not vc_call:
            return await aux.edit("**👉🏻 𝙑𝘾 𝙉𝙤𝙩 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙔𝙚𝙩❗**")
        peer = await client.resolve_peer(chat_id)
        await client.invoke(
            DiscardGroupCall(call=vc_call)
        )
        await aux.edit("**👉🏻 𝙎𝙪𝙘𝙘𝙚𝙨𝙛𝙪𝙡𝙡𝙮 𝙀𝙣𝙙𝙚𝙙 𝙑𝘾. 🌿**")
        await client.invoke(
            CreateGroupCall(
                peer=peer,
                random_id=client.rnd_id() // 9000000000,
            ),
        )
        return await aux.edit("**👉🏻 𝙎𝙪𝙘𝙘𝙚𝙨𝙛𝙪𝙡𝙡𝙮 𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙑𝘾. 🌿**")
    except Exception as e:
        print(f"Error: {e}")
        pass




__NAME__ = "VC"
__MENU__ = """
**Start or End VC in Your Channel
Or Group By Simple Commands.**

`.svc` - Start VC in Your Chat.
`.dvc` - End Vc in Your Chat.
`.rvc` - Restart VC in Your Chat
"""
