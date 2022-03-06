""" Userbot module for other small commands. """
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kyura_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@kyura_cmd(pattern="lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/kyuraxx)"
        "\n[Repo](https://github.com/Kyuraxp/kyura-userbot)"
    )


@kyura_cmd(pattern="vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Kyuraxp/kyura-userbot/kyura-userbot/varshelper.txt)"
    )


CMD_HELP.update(
    {
        "helper": f"`{cmd}lhelp`\
\nUsage: Bantuan Untuk Kyura-Userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
    }
)
