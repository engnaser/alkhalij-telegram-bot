import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

APP_LINK = os.getenv("APP_LINK", "ضع_رابط_التطبيق_هنا")
PHONE_1 = os.getenv("PHONE_1", "775608601")
PHONE_2 = os.getenv("PHONE_2", "781635755")
WHATSAPP_LINK = os.getenv("WHATSAPP_LINK", "https://wa.me/967775608601")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📱 تحميل التطبيق", callback_data="app")],
        [InlineKeyboardButton("💰 شحن الرصيد والباقات", callback_data="balance")],
        [InlineKeyboardButton("🌐 خدمات الإنترنت والفواتير", callback_data="internet")],
        [InlineKeyboardButton("📶 باقات مزايا فورجي", callback_data="four_g")],
        [InlineKeyboardButton("📞 خدمة العملاء", callback_data="support")],
        [InlineKeyboardButton("ℹ️ عن الخليج تيليكوم", callback_data="about")],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "مرحباً بك في بوت الخليج تيليكوم 👋\n\nاختر الخدمة التي تريدها من القائمة التالية:"
    await update.message.reply_text(text, reply_markup=main_menu())

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

async def back_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "اختر الخدمة التي تريدها من القائمة التالية:",
        reply_markup=main_menu()
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "app":
        text = f"📱 تحميل تطبيق الخليج تيليكوم\n\nرابط التطبيق:\n{APP_LINK}"

    elif query.data == "balance":
        text = (
            "💰 شحن الرصيد والباقات\n\n"
            "نوفر خدمات شحن الرصيد والباقات لجميع الشبكات:\n"
            "✅ يمن موبايل\n✅ YOU\n✅ سبأفون\n✅ واي\n\n"
            "للطلب تواصل معنا عبر خدمة العملاء."
        )

    elif query.data == "internet":
        text = (
            "🌐 خدمات الإنترنت والفواتير\n\n"
            "الخدمات المتوفرة:\n"
            "✅ يمن نت\n✅ عدن نت\n✅ يمن فورجي\n✅ تسديد الفواتير\n\n"
            "للاستفسار تواصل معنا."
        )

    elif query.data == "four_g":
        text = (
            "📶 باقات مزايا فورجي\n\n"
            "يمكنك الاستعلام عن باقات يمن فورجي وطلب التفعيل عبر التواصل معنا.\n\n"
            "سيتم إضافة تفاصيل الباقات هنا لاحقاً."
        )

    elif query.data == "support":
        text = (
            "📞 خدمة العملاء\n\n"
            f"اتصال: {PHONE_1} - {PHONE_2}\n"
            f"واتساب: {WHATSAPP_LINK}"
        )

    elif query.data == "about":
        text = (
            "ℹ️ الخليج تيليكوم\n\n"
            "خدمات رقمية، شحن رصيد، باقات، فواتير، إنترنت، وخدمات إلكترونية متنوعة.\n\n"
            "الخليج تيليكوم معك حيثما كنت."
        )
    else:
        text = "اختر خدمة من القائمة."

    await query.edit_message_text(
        text=text,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 رجوع للقائمة", callback_data="back")]])
    )

def run():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing. Add it in Render Environment Variables.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(back_button, pattern="^back$"))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

if __name__ == "__main__":
    run()
