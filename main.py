from flask import Flask
import threading
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)
@app.route('/')
def home():
    return "Guild Bot is Alive!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

threading.Thread(target=run_flask).start()

TOKEN = os.environ.get("BOT_TOKEN")
GUILD_ID = os.environ.get("GUILD_ID", "3107304486")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Online! /guild_info likho")

async def guild_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Guild ID: {GUILD_ID} - Rules Active!")

bot_app = Application.builder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("guild_info", guild_info))
bot_app.run_polling()
