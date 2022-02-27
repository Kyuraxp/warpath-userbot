# ReCode by @Kyuraxx
# FROM Kyura-Userbot <https://github.com/Kyuraxp/kyura-userbot>
# KONTOLLLLLLL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern=r"^\.roast(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**NAJIS  YE JADI ORANG JANGAN CUMA BEBAN KELUARGA, BEBAN NEGARA, BEBAN DUNIA AKHRAT TOLOL,YE KERJA DONGO,KAGA ADA YANG MAU JUGA MERHATIIN ORANG HINA KEK LU SADAR DIRI LU ANAK HARAM**")


@register(outgoing=True, pattern=r"^\.roas1(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GUA TAU KALO LU KAGA PUNYA DUIT BUAT BELI SKINCARE KAN TOLOL ORANG MISKIN KEK LU CUMA BISA MAKE TEPUNG TERIGU, DIKASIH AER BIAR AGAK PUTIHAN JATOHNYA KAGA NGEFEK TOLOL MUKA LU MALAH KEK DONAT BASI BEGO**")


@register(outgoing=True, pattern=r"^\.roas2(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GUA MASIH MENDING BELAJAR TOLOL DARI PADA LO GA PERNAH BELAJAR AHAHA MAKANYA LO ITU MISKIN PENDIDIKAN MISKIN HARTA AHAHA MISKIN EKONOMI SERBA MISKIN KELUARGA LO ANJING AHAHA KOCAK BANGET TOLOL LO ITU PANTES NYA JADI BADUT MAMPANG KALO GA BADUT ANCOL YANG PALANYA GEDE SAMA IDUNH NYA LONJONG UDAH KAYA TIMUN SURI AHAHA JELEK KALO UDAH TUA RETAK DAH TUH SAMA KAYA MUKA LO YA RETAK JAJAR GENJANG DAN TRAPESIUM AHAHAH MENYE BAT MENYEE MAKANYA KALO PUNYA MUKA YANG KERENAN DIKIT LO KAN LAHIR SIA SIA TUHAN JUGA GA NGANGGEP LO HAMBANYA AHAHA KARENA TUHAN LO GHOIB DAN KO JUGA NYEMBAH BATU**")

CMD_HELP.update(
    {
        "war3": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roast\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roas1\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roas2\
        \n↳ : lihat sendiri\
        \n↳ **CEK SENDIRI GAUSAH MANJA!**.\
   "
    }
)
