import telegram.ext
import os

TOKEN = os.environ.get("TOKEN")

def start(update, context):
    update.message.reply_text("Namaste!! Aapka Swagat hai apnebot mein")

def helps(update, context):
    update.message.reply_text("""

    Hi There! I'm Telegram bot created by your loving Priyanshu K Sharma. Please follow these commands:-
                              
                        /start - baatcheet shuru karrne keliye
                        /content - Information about Aadarniya Priyanshu K Sharma
                        /contact - Information about contact
                        /help - To get help from him

                        Aasha hai isse aapki sahayta hogi:)
    
    """)

def content(update, context):
    update.message.reply_text("""

Name: Priyanshu Kumar Sharma
Age: 19 years
Degree: BTech in Cloud Technology and Information Security
College: Ajeenkya D Y Patil University
SEM: 7      Year: 4
    
    """)

def contact(update, context):
    update.message.reply_text("""

    LinkedIN: https://www.linkedin.com/in/priyanshu-kumar-sharma-333800251/
    GitHub: https://github.com/PriyanshuKSharma
    
    """)

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, This is not accepted, please try other command:(")

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", helps))
dispatcher.add_handler(telegram.ext.CommandHandler("content", content))
dispatcher.add_handler(telegram.ext.CommandHandler("contact", contact))

dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
