import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# بيانات بوتك
TOKEN = ("7528729236:AAFPM2yFi6us5hiuD7TWsV5ovs613mXPh6o")
BOT_USERNAME = ("Tr_py_bot")  # بدون @

app = Flask(__name__)

# إعداد البوت
application = ApplicationBuilder().token(TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! هذا بوت Flask على Render ✅")

application.add_handler(CommandHandler("start", start))

# رابط الـ Webhook
@app.route(f"/{BOT_USERNAME}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "ok"

# صفحة للفحص (UptimeRobot)
@app.route("/", methods=["GET"])
def home():
    return "البوت يعمل ✅"

if __name__ == "__main__":
    # لعمل test محلي
    app.run(port=5000)
