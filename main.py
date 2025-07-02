import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد متغيرات البيئة
TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")  # بدون @

# تهيئة Flask و PTB Application
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! البوت يعمل ✅")

application.add_handler(CommandHandler("start", start))

# Route للويب هوك (Webhook)
@app.route(f"/{BOT_USERNAME}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    # استخدم process_update بشكل متزامن مع PTB 20+
    application.create_task(application.process_update(update))
    return "ok"

# Route رئيسي للفحص
@app.route("/", methods=["GET"])
def home():
    return "البوت يعمل ✅"

if __name__ == "__main__":
    # شغّل Flask فقط في التطوير المحلي
    app.run(port=int(os.environ.get("PORT", 5000)))
