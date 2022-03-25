# 🍀 © @kyuraxx
# ⚠️ Do not remove credits
# recode by @Kyuraxx


import random

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kyura_cmd
from userbot import DEFAULTUSER
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@kyura_cmd(pattern="phub$")
async def _(event):
    try:
        phubnya = [
            phub
            async for phub in event.client.iter_messages(
                "@kyuraxphub2", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(phubnya),
            caption=f"Nih kak [{DEFAULTUSER}](tg://user?id={aing.id}) phub nya",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan pornhub.com.")
        
@kyura_cmd(pattern="xxx$")
async def _(event):
    try:
        xxxnya = [
            xxx
            async for xxx in event.client.iter_messages(
                "@kyuraxphub3", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(xxxnya),
            caption=f"Nih kak [{DEFAULTUSER}](tg://user?id={aing.id}) xxx nya",
        )
        await event.delete()
    except Exception:
        await event.edit("tidak bisa menemukan xxx.com.")

@kyura_cmd(pattern="xnxx$")
async def _(event):
    try:
        xnxxnya = [
            xnxx
            async for xnxx in event.client.iter_messages(
                "@kyuraxphub", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(xnxxnya),
            caption=f"Nih kak [{DEFAULTUSER}](tg://user?id={aing.id}) xnxx nya",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan xnxx.")


CMD_HELP.update(
    {
        "phub": f"**Plugin : **`phub`\
        \n\n  •  **Syntax :** `{cmd}phub`\
        \n  •  **Function : **Untuk mengirim pornhub.com secara random.\
        \n\n  •  **Syntax :** `{cmd}xxx`\
        \n  •  **Function : **Untuk mengirim xxx.com secara random.\
        \n\n  •  **Syntax :** `{cmd}xnxx`\
        \n  •  **Function : **Untuk mengirim xnxx.com secara random.\
    "
    }
)
