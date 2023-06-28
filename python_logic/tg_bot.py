import telebot
from data_load import read_data, write_data_to_postgres, read_postgres_to_tg

# Параметры подключения к базе данных PostgreSQL
db_name = 'mydatabase'
user = 'myuser'
password = 'mypassword'
host = 'localhost'
port = '5432'


bot = telebot.TeleBot('6163441421:AAHO1kVI_HTSGefYcRMhV8kDSzcyFNGX9gY')


@bot.message_handler(commands=["report"])
def start(message):

    with open('./answer.xlsx', 'rb') as file:
        bot.send_document(message.chat.id, file)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


columns_name, data = read_data('./Просрочено (06.09.2022).xlsx')
write_data_to_postgres(columns_name, data, db_name, user, password, host, port)
read_postgres_to_tg(db_name, user, password, host, port)

bot.polling(none_stop=True, interval=0)