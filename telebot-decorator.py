import telebot

bot = telebot.TeleBot('YOUR_TOKEN_HERE')

# Варианты вызова bot.message_handler

# Вариант 1 - через декоратор
# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     bot.send_message(message.chat.id, f'hi my creator, you write me an text: {message.text}')

# Вариант 2 - через создание промежуточной функции
# def send_text(message):
#     bot.send_message(message.chat.id, f'hi my creator, you write me an text: {message.text}')
# bind_text = bot.message_handler(content_types=['text'])
# bind_text(send_text)

# Вариант 3 - напрямую
def send_text(message):
    bot.send_message(message.chat.id, f'hi my creator, you write me an text: {message.text}')
bot.message_handler(content_types=['text'])(send_text)

bot.polling()
