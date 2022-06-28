import re
from flask import Flask, request
import telegram

from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters



global TOKEN
TOKEN = "722754489:AAHxkLS09862htj0c4E5VEcNvJMjOSNXL_k"

app = Flask(__name__)

application = Application.builder().token(TOKEN).build()

def start(update, context):
    update.message.reply_text("Hello, I am a bot")

    
application.add_handler(CommandHandler('start', start))


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def respond(path):
    path = path.replace('%', ':')
    print(path)
    # retrieve the message in JSON and then transform it to Telegram object
    update = request.get_json()
    print(update)
    Application.process_update(self=application, update=update)
    
    return 'ok'


if __name__ == '__main__':
       app.run(port=8443, ssl_context=('C:\\Users\\abdoN\\botmaker\\venv\\cert.pem', r'C:\\Users\\abdoN\\botmaker\\venv\\private.key'))