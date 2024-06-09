import telebot
from flask import Flask, request
token ='6863061604:AAFa6R1qOjNjZxP6HUdUPjbcZaFRaW8Jo8o'
secret='ioufbvewgr2492yf2gh'

url = 'https://vps-3503468-x.dattaweb.com/ + secret'
bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)


app = Flask(__name__)
@app.route('/'+secret,methods= ['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Hello, welcome to test bot!")

@bot.message_handler(commands=['help'])
def help(m):
    bot.send_message(m.chat.id, 'If you need help, try again later')

    
@bot.message_handler(content_types=['text'])
def echo(m):
    bot.send_message(m.chat.id, m. text)
    
@bot.message_handler(content_types=['photo'])
def photo(m):
    bot.send_message(m.chat.id, 'Nice photo!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)