from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["fr", "rr", "rraid", "fuckraid"]))
@sudo_users_only
async def add_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜 ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**👉🏻 𝙍𝙚𝙥𝙡𝙮 𝙩𝙤 𝙖 𝙪𝙨𝙚𝙧'𝙨 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙤𝙧 𝙜𝙞𝙫𝙚 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚/𝙪𝙨𝙚𝙧_𝙞𝙙 🫠.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id

        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 𝙗𝙡𝙤𝙤𝙙𝙮 𝙁𝙤𝙤𝙡, 𝙒𝙝𝙮 𝙙𝙤 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚 𝙍𝙚𝙥𝙡𝙮 𝙍𝙖𝙞𝙙 𝙊𝙣 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣 𝙄𝘿 😡❓**"
            )
        
        fraid = await add_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**💥 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝘼𝙙𝙙𝙚𝙙 𝙍𝙚𝙥𝙡𝙮 𝙍𝙖𝙞𝙙 𝙊𝙣 𝙏𝙝𝙞𝙨 𝙐𝙨𝙚𝙧 😍.**"
            )
        return await aux.edit(
            "**👉🏻 𝘿𝙪𝙙𝙚, 𝙍𝙚𝙥𝙡𝙮 𝙍𝙖𝙞𝙙 𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝘼𝙘𝙩𝙞𝙫𝙚 𝙊𝙣 𝙏𝙝𝙞𝙨 𝙐𝙨𝙚𝙧 🌸**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dfr", "drr", "drraid", "dfuckraid"]))
@sudo_users_only
async def del_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜 ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**👉🏻 𝙍𝙚𝙥𝙡𝙮 𝙩𝙤 𝙖 𝙪𝙨𝙚𝙧'𝙨 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙤𝙧 𝙜𝙞𝙫𝙚 𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚/𝙪𝙨𝙚𝙧_𝙞𝙙 😇.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 𝘽𝙡𝙤𝙤𝙙𝙮 𝙁𝙤𝙤𝙡, 𝙒𝙝𝙮 𝘿𝙤 𝙪 𝙒𝙖𝙣𝙩 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚 𝙍𝙚𝙥𝙡𝙮 𝙍𝙖𝙞𝙙 𝙊𝙣 𝙔𝙤𝙪𝙧 𝙄𝘿❓**"
            )
        
        fraid = await del_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**👉🏻 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙍𝙚𝙢𝙤𝙫𝙚𝙙 𝙍𝙚𝙥𝙡𝙮 𝙍𝙖𝙞𝙙 𝙁𝙧𝙤𝙢 𝙏𝙝𝙞𝙨 𝙐𝙨𝙚𝙧 ⚡.**"
            )
        return await aux.edit(
            "**👉🏻 𝘿𝙪𝙙𝙚, 𝙍𝙚𝙥𝙡𝙮 𝙍𝙖𝙞𝙙 𝙉𝙤𝙩 𝘼𝙘𝙩𝙞𝙫𝙖𝙩𝙚𝙙 𝙊𝙣 𝙏𝙝𝙞𝙨 𝙐𝙨𝙚𝙧 😿**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
