# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

"""Userbot module for keeping control who PM you."""

from sqlalchemy.exc import IntegrityError
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.types import User

from userbot import CMD_HANDLER as cmd
from userbot import (
    ALIVE_LOGO,
    ALIVE_NAME,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    COUNT_PM,
    LASTMSG,
    LOGS,
    PM_AUTO_BAN,
    PM_LIMIT,
    PMPERMIT_PIC,
    PMPERMIT_TEXT,
)
from userbot.events import register
from userbot.utils import kyura_cmd

if PMPERMIT_PIC is None:
    CUSTOM_PIC = ALIVE_LOGO
else:
    CUSTOM_PIC = str(PMPERMIT_PIC)

COUNT_PM = {}
LASTMSG = {}


# ========================= CONSTANTS ============================

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
CUSTOM_TEXT = (
    str(PMPERMIT_TEXT)
    if PMPERMIT_TEXT
    else f"__Hi Tod, saya bot ✫AM͢͢͢ITOD-U฿OT yang menjaga room chat {DEFAULTUSER} di mohon jangan melakukan spam ya tod, kalau lu melakukan itu OTOMATIS gw akan memblockir lu ya tod!__ \n"
)
DEF_UNAPPROVED_MSG = (
    "➠ PERINGATAN YA❗\n"

    "“𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐓𝐡𝐞 𝐏𝐫𝐢𝐯𝐚𝐜𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞”\n"

    "Ini Hanya Pesan Dari Bot!\n" 

    "Masa Lu Baper Ama Bot Wkwkwk\n"

    "╔══════════════════════╗\n"

    "╠•Hai Tod Lu Gay Ya?Dih Si Gay\n"

    "╠•Canda Tod.Chat Gw Harus Ganteng\n"

    "╠•Oi Tod Kerana Lu Gak Ganteng\n"

    "╠•Gw Belum Menyetujui Lu\n"

    "╠•Tunggu Sampai Lu Ganteng\n"

    "╠•Baru Gw Menyetujui Chat\n"

    "╠•Dari Lu Jadi Kalau Gw\n"

    "╠•Gak Balas Lagi Chat Lu\n"

    "╠•Jangan Lu Spam Chat Ya Anj\n"

    "╠•Kek Org Tolol Gak Bisa Baca\n"

    "╠•Atau Lu Akan Otomatis Terblokir.\n"

    "╚══════════════════════╝\n"

    "╭✠╼━━━━━━❖━━━━━━━✠╮

    "┣[•𖣘 AUTOREPLAY MASSAGES

    "┣[•𖣘 BY: AmiUser-iBotz

    "┣[•𖣘 AMIBOT: @amibaik_bot

    "╰✠╼━━━━━━❖━━━━━━━✠╯

    "╭✠╼━━━━━━❖━━━━━━━✠╮\n"

    "┣[•𖣘 **𝗦𝘂𝗽𝗽𝗼𝗿𝘁: @AmiBotSiMurni**\n"

    "┣[•𖣘 **𝗖𝗵𝗮𝗻𝗻𝗲𝗹: @amAllservice**\n"

    "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
)
# =================================================================


@register(incoming=True, disable_edited=True, disable_errors=True)
async def permitpm(event):
    """Prohibits people from PMing you without approval. \
        Will block retarded nibbas automatically."""
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    if (
        event.is_private
        and event.chat_id != 777000
        and event.chat_id != self_user.id
        and not (await event.get_sender()).bot
    ):
        try:
            from userbot.modules.sql_helper.globals import gvarstatus
            from userbot.modules.sql_helper.pm_permit_sql import is_approved
        except AttributeError:
            return
        apprv = is_approved(event.chat_id)
        notifsoff = gvarstatus("NOTIF_OFF")

        # Use user custom unapproved message
        getmsg = gvarstatus("unapproved_msg")
        if getmsg is not None:
            UNAPPROVED_MSG = getmsg
        else:
            UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

        # This part basically is a sanity check
        # If the message that sent before is Unapproved Message
        # then stop sending it again to prevent FloodHit
        if not apprv and event.text != UNAPPROVED_MSG:
            if event.chat_id in LASTMSG:
                prevmsg = LASTMSG[event.chat_id]
                # If the message doesn't same as previous one
                # Send the Unapproved Message again
                if event.text != prevmsg:
                    async for message in event.client.iter_messages(
                        event.chat_id, from_user="me", search=UNAPPROVED_MSG
                    ):
                        await message.delete()
                    await event.reply(f"{UNAPPROVED_MSG}")
            else:
                await event.reply(f"{UNAPPROVED_MSG}")
            LASTMSG.update({event.chat_id: event.text})
            if notifsoff:
                await event.client.send_read_acknowledge(event.chat_id)
            if event.chat_id not in COUNT_PM:
                COUNT_PM.update({event.chat_id: 1})
            else:
                COUNT_PM[event.chat_id] = COUNT_PM[event.chat_id] + 1

            if COUNT_PM[event.chat_id] > PM_LIMIT:
                await event.respond(
                    "`UDAH JELEK LU BODO LAGI GW BLOCK LU KARNA NGESPAM`\n"
                    f"`KE OWNER GW!!`"
                )

                try:
                    del COUNT_PM[event.chat_id]
                    del LASTMSG[event.chat_id]
                except KeyError:
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            "Terjadi Masalah Saat Menghitung Private Message, Mohon Restart Bot!",
                        )
                    return LOGS.info("CountPM wen't rarted boi")

                await event.client(BlockRequest(event.chat_id))
                await event.client(ReportSpamRequest(peer=event.chat_id))

                if BOTLOG:
                    name = await event.client.get_entity(event.chat_id)
                    name0 = str(name.first_name)
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "["
                        + name0
                        + "](tg://user?id="
                        + str(event.chat_id)
                        + ")"
                        + " Mampus Gw Block Lu Jelek Kali Muka Lu",
                    )


@register(disable_edited=True, outgoing=True, disable_errors=True)
async def auto_accept(event):
    """Will approve automatically if you texted them first."""
    if not PM_AUTO_BAN:
        return
    self_user = await event.client.get_me()
    if (
        event.is_private
        and event.chat_id != 777000
        and event.chat_id != self_user.id
        and not (await event.get_sender()).bot
    ):
        try:
            from userbot.modules.sql_helper.globals import gvarstatus
            from userbot.modules.sql_helper.pm_permit_sql import approve, is_approved
        except AttributeError:
            return

        # Use user custom unapproved message
        get_message = gvarstatus("unapproved_msg")
        if get_message is not None:
            UNAPPROVED_MSG = get_message
        else:
            UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

        chat = await event.get_chat()
        if isinstance(chat, User):
            if is_approved(event.chat_id) or chat.bot:
                return
            async for message in event.client.iter_messages(
                event.chat_id, reverse=True, limit=1
            ):
                if (
                    message.text is not UNAPPROVED_MSG
                    and message.from_id == self_user.id
                ):
                    try:
                        approve(event.chat_id)
                    except IntegrityError:
                        return

                if is_approved(event.chat_id) and BOTLOG:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        "#AUTO-APPROVED\n"
                        + "Pengguna: "
                        + f"[{chat.first_name}](tg://user?id={chat.id})",
                    )


@kyura_cmd(pattern="notifoff$")
async def notifoff(noff_event):
    """For .notifoff command, stop getting notifications from unapproved PMs."""
    try:
        from userbot.modules.sql_helper.globals import addgvar
    except AttributeError:
        return await noff_event.edit("`Running on Non-SQL mode!`")
    addgvar("NOTIF_OFF", True)
    await noff_event.edit(
        "`Notifikasi Dari Pesan Pribadi Tidak Disetujui, Telah Dibisukan!`"
    )


@kyura_cmd(pattern="notifon$")
async def notifon(non_event):
    """For .notifoff command, get notifications from unapproved PMs."""
    try:
        from userbot.modules.sql_helper.globals import delgvar
    except AttributeError:
        return await non_event.edit("`Running on Non-SQL mode!`")
    delgvar("NOTIF_OFF")
    await non_event.edit(
        "`Notifikasi Dari Pesan Pribadi Tidak Disetujui, Tidak Lagi Dibisukan!`"
    )


@kyura_cmd(pattern="(?:setuju|ok)\s?(.)?")
async def approvepm(apprvpm):
    """For .ok command, give someone the permissions to PM you."""
    try:
        from userbot.modules.sql_helper.globals import gvarstatus
        from userbot.modules.sql_helper.pm_permit_sql import approve
    except AttributeError:
        return await apprvpm.edit("`Running on Non-SQL mode!`")

    if apprvpm.reply_to_msg_id:
        reply = await apprvpm.get_reply_message()
        replied_user = await apprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id

    else:
        aname = await apprvpm.client.get_entity(apprvpm.chat_id)
        name0 = str(aname.first_name)
        uid = apprvpm.chat_id

    # Get user custom msg
    getmsg = gvarstatus("unapproved_msg")
    if getmsg is not None:
        UNAPPROVED_MSG = getmsg
    else:
        UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

    async for message in apprvpm.client.iter_messages(
        apprvpm.chat_id, from_user="me", search=UNAPPROVED_MSG
    ):
        await message.delete()

    try:
        approve(uid)
    except IntegrityError:
        return await apprvpm.edit("`Karna Gw Baik Gw Terima Pesan lu`")

    await apprvpm.edit(
        f"`Hai Tod` [{name0}](tg://user?id={uid}) `Pesan Lu Sudah Diterima Nih Oleh Owner Gw`"
    )
    await apprvpm.delete(getmsg)
    await message.delete()

    if BOTLOG:
        await apprvpm.client.send_message(
            BOTLOG_CHATID, "#DITERIMA\n" + "User: " + f"[{name0}](tg://user?id={uid})"
        )


@kyura_cmd(pattern="(?:tolak|nopm)\s?(.)?")
async def disapprovepm(disapprvpm):
    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove
    except BaseException:
        return await disapprvpm.edit("`Running on Non-SQL mode!`")

    if disapprvpm.reply_to_msg_id:
        reply = await disapprvpm.get_reply_message()
        replied_user = await disapprvpm.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        dissprove(aname)
    else:
        dissprove(disapprvpm.chat_id)
        aname = await disapprvpm.client.get_entity(disapprvpm.chat_id)
        name0 = str(aname.first_name)

    await disapprvpm.edit(
        f"`Maaf Ya Lu Terlalu Jelek` [{name0}](tg://user?id={disapprvpm.chat_id}) `Jadi Gw Tolak Pesan Lu, Mohon Jangan Melakukan Spam Ya Tod Di Room Chat Gw!`"
    )

    if BOTLOG:
        await disapprvpm.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={disapprvpm.chat_id})" " `Berhasil Ditolak Ya Tod` !",
        )


@kyura_cmd(pattern="block$")
async def blockpm(block):
    """For .block command, block people from PMing you!"""
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client.get_entity(reply.from_id)
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        await block.client(BlockRequest(aname))
        await block.edit(f"`Maaf Kamu Terlalu Sombong Jadi Kamu Telah Diblokir! Oleh {DEFAULTUSER}`")
        uid = replied_user.id
    else:
        await block.client(BlockRequest(block.chat_id))
        aname = await block.client.get_entity(block.chat_id)
        await block.edit(f"`Dih Karna Lu Jelek Gw Block Lu Mampus!`")
        name0 = str(aname.first_name)
        uid = block.chat_id

    try:
        from userbot.modules.sql_helper.pm_permit_sql import dissprove

        dissprove(uid)
    except AttributeError:
        pass

    if BOTLOG:
        await block.client.send_message(
            BOTLOG_CHATID,
            "#BLOKIR\n" + "Pengguna: " + f"[{name0}](tg://user?id={uid})",
        )


@kyura_cmd(pattern="unblock$")
async def unblockpm(unblock):
    """For .unblock command, let people PMing you again!"""
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client.get_entity(reply.from_id)
        name0 = str(replied_user.first_name)
        await unblock.client(UnblockRequest(replied_user.id))
        await unblock.edit("`Karna Gw Baik Gw Buka Blocknya Ya Tod.`")

    if BOTLOG:
        await unblock.client.send_message(
            BOTLOG_CHATID,
            f"[{name0}](tg://user?id={replied_user.id})" " Woy Tod Lu Tidak Lagi Diblokir.",
        )


@kyura_cmd(pattern="(set|get|reset) pm_msg(?: |$)(\w*)")
async def add_pmsg(cust_msg):
    """Set your own Unapproved message"""
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            "**Anda Harus Menyetel** `PM_AUTO_BAN` **Ke** `True` Atau Ketik `.set var PM_AUTO_BAN True`"
        )
    try:
        import userbot.modules.sql_helper.globals as sql
    except AttributeError:
        await cust_msg.edit("`Running on Non-SQL mode!`")
        return

    await cust_msg.edit("`Sedang Memproses...`")
    conf = cust_msg.pattern_match.group(1)

    custom_message = sql.gvarstatus("unapproved_msg")

    if conf.lower() == "set":
        message = await cust_msg.get_reply_message()
        status = "Pesan"

        # check and clear user unapproved message first
        if custom_message is not None:
            sql.delgvar("unapproved_msg")
            status = "Pesan"

        if message:
            # TODO: allow user to have a custom text formatting
            # eg: bold, underline, striketrough, link
            # for now all text are in monoscape
            msg = message.message  # get the plain text
            sql.addgvar("unapproved_msg", msg)
        else:
            return await cust_msg.edit("`Mohon Balas Ke Pesan`")

        await cust_msg.edit("`Pesan Berhasil Disimpan Ke Room Chat`")

        if BOTLOG:
            await cust_msg.client.send_message(
                BOTLOG_CHATID,
                f"**{status} PM Yang Tersimpan Dalam Room Chat Anda:** \n\n{msg}",
            )

    if conf.lower() == "reset":
        if custom_message is not None:
            sql.delgvar("unapproved_msg")
            await cust_msg.edit("`Anda Telah Menghapus Pesan Custom PM Ke Default`")
        else:
            await cust_msg.edit("`Pesan PM Anda Sudah Default Sejak Awal`")

    if conf.lower() == "get":
        if custom_message is not None:
            await cust_msg.edit(
                "**Ini Adalah Pesan PM Yang Sekarang Dikirimkan Ke Room Chat Anda:**"
                f"\n\n{custom_message}"
            )
        else:
            await cust_msg.edit(
                "*Anda Belum Menyetel Pesan PM*\n"
                f"Masih Menggunakan Pesan PM Default: \n\n`{DEF_UNAPPROVED_MSG}`"
            )


@register(
    incoming=True, disable_edited=True, disable_errors=True, from_users=(1282429349)
)
async def permitpm(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pm_permit_sql.is_approved(chats.id):
            pm_permit_sql.approve(
                chats.id, f"`{ALIVE_NAME} Telah Mengirimi Anda Pesan 😯`"
            )
            await borg.send_message(
                chats, f"**Menerima Pesan!, Pengguna Terdeteksi Adalah {DEFAULTUSER}**"
            )


CMD_HELP.update(
    {
        "pmpermit": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}setuju | {cmd}ok`"
        "\n↳ : Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}tolak | .nopm`"
        "\n↳ : Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}block`"
        "\n↳ : Memblokir Orang Di PM."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}unblock`"
        "\n↳ : Membuka Blokir."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}notifoff`"
        "\n↳ : Mematikan notifikasi pesan yang belum diterima."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}notifon`"
        "\n↳ : Menghidupkan notifikasi pesan yang belum diterima."
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}set pm_msg` <balas ke pesan>"
        "\n↳ : Menyetel Pesan Pribadimu untuk orang yang pesannya belum diterima"
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}get pm_msg`"
        "\n↳ : Mendapatkan Custom pesan PM mu"
        f"\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: >`{cmd}reset pm_msg`"
        "\n↳ : Menghapus pesan PM ke default"
        "\n\nPesan Pribadi yang belum diterima saat ini tidak dapat disetel"
        "\nke teks format kaya bold, underline, link, dll."
        "\nPesan akan terkirim normal saja"
    }
)
