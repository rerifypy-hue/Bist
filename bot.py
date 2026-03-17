import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")

async def sinyal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /sinyal THYAO")
        return

    ticker = context.args[0]

    res = requests.get(f"{API_URL}/signal/{ticker}")
    data = res.json()

    await update.message.reply_text(
        f"{ticker} → {data['signal']}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("sinyal", sinyal))

app.run_polling()
