from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID

async def forward_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user = update.message.from_user
    if user.id == ADMIN_ID:
        return

    caption = f"پیام از {user.first_name} (@{user.username or 'NoUsername'})"

    if update.message.text:
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"{caption}:\n{update.message.text}")
    elif update.message.photo:
        await context.bot.send_photo(chat_id=ADMIN_ID, photo=update.message.photo[-1].file_id, caption=caption)
    elif update.message.video:
        await context.bot.send_video(chat_id=ADMIN_ID, video=update.message.video.file_id, caption=caption)
    elif update.message.audio:
        await context.bot.send_audio(chat_id=ADMIN_ID, audio=update.message.audio.file_id, caption=caption)
    elif update.message.document:
        await context.bot.send_document(chat_id=ADMIN_ID, document=update.message.document.file_id, caption=caption)