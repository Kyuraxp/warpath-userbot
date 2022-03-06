from time import sleep

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kyura_cmd


@kyura_cmd(pattern="ngentot(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**WOYY NGENTOD!!**")
    sleep(1)
    await typew.edit("**JANGAN SOK JAGOAN DAH LU**")
    sleep(1)
    await typew.edit("**MUKA MASIH KAYA KONTOL AJA**")
    sleep(1)
    await typew.edit("**BANGGA LU HAHAHAHA**")
    sleep(1)
    await typew.edit("**COBA DEH NGACA MUKA LU KAN HINA BANGET**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")
    sleep(1)
    await typew.edit("**MAKANYA GANTENG KONTOL**")
    sleep(1)
    await typew.edit("**BIAR MUKALU GAK DIHINA TERUS**")
    sleep(1)
    await typew.edit("**SAMA ORANG LAIN**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")


# Create by myself @localheart


@kyura_cmd(pattern="goblok(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**WOYY GOBLOK!!**")
    sleep(1)
    await typew.edit("**KO LU GOBLOK BANGET SIH**")
    sleep(1)
    await typew.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(1)
    await typew.edit("**YANG LEMBEK KETIKA LEMAH**")
    sleep(1)
    await typew.edit("**DAN KERAS KETIKA LU SANGE GOBLOK**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")
    sleep(1)
    await typew.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(1)
    await typew.edit("**MUKA LU AJA KAYA ASPAL JALANAN**")
    sleep(1)
    await typew.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")


# Create by myself @localheart


@kyura_cmd(pattern="ngatain(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**BABI!!**")
    sleep(1)
    await typew.edit("**MUKA LU KAYA BABI**")
    sleep(1)
    await typew.edit("**OTAK LU TUH KAYA KONTOL**")
    sleep(1)
    await typew.edit("**MUKA LU HINA BANGET**")
    sleep(1)
    await typew.edit("**OTAK LU KAYA BATU**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")
    sleep(1)
    await typew.edit("**MAKANYA JANGAN SANGEAN MULU**")
    sleep(1)
    await typew.edit("**KONTOL LU AJA MASIH BENGKOK**")
    sleep(1)
    await typew.edit("**EHHH SANGE NYA MAU DAPAT YANG CANTIK**")
    sleep(1)
    await typew.edit("**HAHAHAHA**")


# Create by myself @localheart

CMD_HELP.update(
    {
        "toxic2": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ngentot`\
    \n↳ : Lu Coba Sendiri Aja."
        f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}goblok`\
    \n↳ : Lu Coba Sendiri Aja."
        f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ngatain`\
    \n↳ : Lu Coba Sendiri Aja."
    }
)
