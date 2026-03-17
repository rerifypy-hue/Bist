import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8377301703:AAEXlRxIzbMIB0A4yvKjvaXNWn2dkQjOMp4"
API_URL = "https://worker-production-1b5d.up.railway.app"

async def sinyal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Kullanım: /sinyal THYAO")
        return

    ticker = context.args[0].upper()  # Büyük harf yap
    try:
        res = requests.get(f"{API_URL}/signal/{ticker}")
        res.raise_for_status()  # HTTP hatalarını yakalar
        data = res.json()
    except requests.exceptions.RequestException:
        await update.message.reply_text("API isteği sırasında bir hata oluştu.")
        return
    except ValueError:
        await update.message.reply_text("API geçersiz JSON döndürdü.")
        return

    signal = data.get("signal")
    if signal:
        await update.message.reply_text(f"{ticker} → {signal}")
    else:
        await update.message.reply_text(f"{ticker} için sinyal bulunamadı.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("sinyal", sinyal))
    print("Bot çalışıyor...")
    app.run_polling()