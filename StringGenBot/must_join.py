from config import MUST_JOIN

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/cce8a46326e6067f0d88c.jpg", caption=f"» 𝓓𝓾𝓮 𝓣𝓸 𝓸𝓿𝓮𝓻𝓵𝓸𝓪𝓭 𝓞𝓷𝓵𝔂 𝓜𝔂 𝓒𝓱𝓪𝓷𝓷𝓮𝓵𝓼 𝓢𝓾𝓫𝓼 𝓒𝓪𝓷 𝓤𝓼𝓮 𝓜𝓮 !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🇮🇳JOIN Channel🤷🏻‍♂️", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
