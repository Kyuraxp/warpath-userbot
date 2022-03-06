# ReCode by @Kyuraxx
# FROM Kyura-Userbot <https://github.com/Kyuraxp/kyura-userbot>
# KONTOLLLLLLL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import kyura_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@kyura_cmd(pattern="roast(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**NAJIS  YE JADI ORANG JANGAN CUMA BEBAN KELUARGA, BEBAN NEGARA, BEBAN DUNIA AKHRAT TOLOL,YE KERJA DONGO,KAGA ADA YANG MAU JUGA MERHATIIN ORANG HINA KEK LU SADAR DIRI LU ANAK HARAM**")


@kyura_cmd(pattern="roas1(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GUA TAU KALO LU KAGA PUNYA DUIT BUAT BELI SKINCARE KAN TOLOL ORANG MISKIN KEK LU CUMA BISA MAKE TEPUNG TERIGU, DIKASIH AER BIAR AGAK PUTIHAN JATOHNYA KAGA NGEFEK TOLOL MUKA LU MALAH KEK DONAT BASI BEGO**")


@kyura_cmd(pattern="roas2(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GUA MASIH MENDING BELAJAR TOLOL DARI PADA LO GA PERNAH BELAJAR AHAHA MAKANYA LO ITU MISKIN PENDIDIKAN MISKIN HARTA AHAHA MISKIN EKONOMI SERBA MISKIN KELUARGA LO ANJING AHAHA KOCAK BANGET TOLOL LO ITU PANTES NYA JADI BADUT MAMPANG KALO GA BADUT ANCOL YANG PALANYA GEDE SAMA IDUNH NYA LONJONG UDAH KAYA TIMUN SURI AHAHA JELEK KALO UDAH TUA RETAK DAH TUH SAMA KAYA MUKA LO YA RETAK JAJAR GENJANG DAN TRAPESIUM AHAHAH MENYE BAT MENYEE MAKANYA KALO PUNYA MUKA YANG KERENAN DIKIT LO KAN LAHIR SIA SIA TUHAN JUGA GA NGANGGEP LO HAMBANYA AHAHA KARENA TUHAN LO GHOIB DAN KO JUGA NYEMBAH BATU**")

    
@kyura_cmd(pattern="roas3(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1) 
    await typew.edit(
        "**POHON KARET WKWK KOCAH LO MENDING JADI SUPER MARIO AJA NOH BILANG KE KAKE NENEK LO MENDING JADI SUPER MARIO KALO GA LOST SAGA HAHA JADI BOCAH POINT BLANK DIA BOLOT ANJING AHAHA MAKANYA KALO PUNYA KUPING YANG BENERAN DIKIT TOLOL KUPING LO CONGE NYA BLEBERAN SAMPE LUAR LUAR KALI YA AHAHA KASIHAN BANGET GUA LIAT LO BERPENYAKITAN SEGALA MACEM ADA WKWK DAN BURUK NYA LO TUH LO UDAH KAYA LEAK GITU UDAH ITU MULUT UDAH KAYA JULUNG JULUNG GITU JELEK BANGET KAYA NUGET GITU YA MUKA LO BIBIR LO SUMBING YA APA DOBLEH AHAHAH**")
    
CMD_HELP.update(
    {
        "war3": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}roast\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}roas1\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}roas2\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: {cmd}roas3\
        \n↳ : lihat sendiri\
        \n↳ **CEK SENDIRI GAUSAH MANJA!**.\
   "
    }
)
