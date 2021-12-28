import telebot # Importamos las librería
TOKEN = "5035305575:AAF0CZbYK-pOETL1mGU0x8TX1U4TEaT4R0Q" # Ponemos nuestro Token generado con el @BotFather
bot = telebot.TeleBot(TOKEN)  #Creamos nuestra instancia "bot" a partir de ese TOKEN



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "¿Me ha llamado maestro?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()