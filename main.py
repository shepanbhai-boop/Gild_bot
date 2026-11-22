from telegram.ext import Application, CommandHandler
from telegram import Update

TOKEN = "9201047717:AAGbcYJ7VaT7Pypy3vKN10Jno1pYEwpd7Gg"

async def start(update: Update, context):
    await update.message.reply_text("Guild Bot Online! 👑 /guild_info")

async def guild_info(update: Update, context):
    await update.message.reply_text("Guild Rules: Active থাকতে হবে।")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("guild_info", guild_info))
app.run_polling()
