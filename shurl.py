import requests
import telebot

bot = telebot.TeleBot('1748363763:AAHV2sHqyxngs_mmmE6XaH8DPN2xGNK8zBk')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'link shorter by shurl.ml 🌋')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'private':
        url = requests.get("http://shurl.ml/api?url="+message.text)
        if url.text == "Error":
            bot.send_message(message.chat.id, "Uncorrect URL!")
        else:
            bot.send_message(message.chat.id, "Your link 🎨: "+"<pre>"+url.text+"</pre>", parse_mode="html")

bot.polling()