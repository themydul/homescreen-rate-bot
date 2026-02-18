import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8561488954:AAECu2_Kwtkw6tSlh6a6tEauRi_1akANP84"

async def rate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").lower()

    # If user sends photo
    if update.message.photo:
        rating = random.randint(0, 10)
        await update.message.reply_text(f"🔥 Home Screen Rate: {rating}/10")

    # If message contains "rate"
    elif "rate" in text:
        rating = random.randint(0, 10)
        await update.message.reply_text(f"🔥 Home Screen Rate: {rating}/10")


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.PHOTO | filters.TEXT, rate_image))

app.run_polling()
