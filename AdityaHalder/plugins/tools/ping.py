from ... import *
from datetime import datetime

@app.on_message(cdx("ping"))
@sudo_users_only
async def ping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    m = await eor(message, "**💥 ₱ł₦₲ !**")
    await m.edit(f"**⚡ 𝙥𝙞𝙣𝙜𝙚𝙙 !\n𝙡𝙖𝙩𝙚𝙣𝙘𝙮:** `{ms}` 𝙢𝙨")



__NAME__ = "𝙋𝙞𝙣𝙜⚡"
__MENU__ = """
`.ping` - **𝙫𝙚𝙧𝙞𝙛𝙮 𝙋𝙞𝙣𝙜 𝙇𝙖𝙩𝙚𝙣𝙘𝙮
𝙊𝙛 𝙔𝙤𝙪𝙧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙨𝙚𝙧𝙫𝙚𝙧 ❤.**
"""
