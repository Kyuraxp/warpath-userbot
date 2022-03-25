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
                "@kyuraxphub", filter=InputMessagesFilterVoice
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
        await event.edit("Tidak bisa menemukan porn.hub.")
        
@kyura_cmd(pattern="phub2$")
async def _(event):
    try:
        phubnya = [
            phub
            async for phub in event.client.iter_messages(
                "@kyuraxphub", filter=InputMessagesFilterPhotos
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
        await event.edit("tidak bisa menemukan porn.hub.")

@kyura_cmd(pattern="phub3$")
async def _(event):
    try:
        phubnya = [
            phub
            async for phub in event.client.iter_messages(
                "@kyuraxphub", filter=InputMessagesFilterVideo
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
        await event.edit("Tidak bisa menemukan phub.")


CMD_HELP.update(
    {
        "phub": f"**Plugin : **`phub`\
        \n\n  •  **Syntax :** `{cmd}phub`\
        \n  •  **Function : **Untuk mengirim porn.hub secara random.\
        \n\n  •  **Syntax :** `{cmd}phub2`\
        \n  •  **Function : **Untuk mengirim porn.hub secara random.\
        \n\n  •  **Syntax :** `{cmd}phub3`\
        \n  •  **Function : **Untuk mengirim porn.hub secara random.\
    "
    }
)
