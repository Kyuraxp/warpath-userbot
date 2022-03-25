from telethon.errors import PeerIdInvalidError, YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename, DocumentAttributeSticker
from telethon.utils import get_input_document

from . import (
    KANGING_STR,
    LOGS,
    asst,
    async_searcher,
    bash,
    con,
    functions,
    get_string,
    inline_mention,
    mediainfo,
    quotly,
    types,
    udB,
    kyura_cmd,
)


@kyura_cmd(pattern="packkang")
async def pack_kangish(_):
    _e = await _.get_reply_message()
    if not (_e and _e.sticker and _e.file.mime_type == "image/webp"):
        return await _.eor(get_string("sts_4"))
    if len(_.text) > 9:
        _packname = _.text.split(" ", maxsplit=1)[1]
    else:
        _packname = f",Kyura-Userbot Kang Pack By {_.sender_id}"
    _id = _e.media.document.attributes[1].stickerset.id
    _hash = _e.media.document.attributes[1].stickerset.access_hash
    _get_stiks = await _.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetID(id=_id, access_hash=_hash), hash=0
        )
    )
    stiks = []
    for i in _get_stiks.documents:
        x = get_input_document(i)
        stiks.append(
            types.InputStickerSetItem(
                document=x,
                emoji=(i.attributes[1]).alt,
            )
        )
    try:
        short_name = "ult_" + _packname.replace(" ", "_") + str(_.id)
        _r_e_s = await asst(
            functions.stickers.CreateStickerSetRequest(
                user_id=_.sender_id,
                title=_packname,
                short_name=f"{short_name}_by_{asst.me.username}",
                stickers=stiks,
            )
        )
    except PeerIdInvalidError:
        return await _.eor(
            f"Hey {inline_mention(_.sender)} send `/start` to @{asst.me.username} and later try this command again.."
        )
    except BaseException as er:
        LOGS.exception(er)
        return await _.eor(str(er))
    await _.eor(
        get_string("sts_5").format(f"https://t.me/addstickers/{_r_e_s.set.short_name}"),
    )
