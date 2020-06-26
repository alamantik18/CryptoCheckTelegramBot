import telebot
import constants
import symbols

def main():
    bot=telebot.TeleBot(constants.token)
    names = symbols.parse()[0][0::5]
    fast_name = symbols.parse()[0][1::5]
    list_mass = [names[i] + " => " + fast_name[i] for i in range(0, 200)]
    hour = symbols.parse()[0][2::5]
    day = symbols.parse()[0][3::5]
    week = symbols.parse()[0][4::5]
    print(symbols.parse())
    #fast_name = [element.lower() for element in fast_name]

    @bot.message_handler(commands=['start'])
    def handler_start(message):
        user_markup=telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('BTC', 'ETH')
        user_markup.row('ETC', 'XRP')
        user_markup.row('list')
        bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)

    @bot.message_handler(commands=['stop'])
    def handler_start(message):
        hide_markup=telebot.types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, '((', reply_markup=hide_markup)

    @bot.message_handler(commands=['help'])
    def handler_help(message):
        bot.send_message(message.from_user.id,
                         "Бот создан для быстрого просмотра цен на криптовалюты. В базе бота собрано всего 200 возможных валют. Для просмотра цены отправь мне символьное название криптовалюты, например 'btc'.")

    @bot.message_handler(commands=['list'])
    def handler_list(message):
        bot.send_message(message.from_user.id, "Список всех валют:\n" + str(list_mass))

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text.upper() == 'ПРИВЕТ':
            bot.send_message(message.from_user.id, 'Да да, я тут.')
        elif message.text.upper() in fast_name:
            price = symbols.parse()[1]
            bot.send_message(message.from_user.id, "Цена на " + names[fast_name.index(message.text.upper())] + "(" + fast_name[fast_name.index(message.text.upper())] +")" + " = " + price[fast_name.index(message.text.upper())])
            bot.send_message(message.from_user.id, "Изменения за час: " + hour[fast_name.index(message.text.upper())] + "\nИзменения за день: " + day[fast_name.index(message.text.upper())] + "\nИзменения за неделю: " + week[fast_name.index(message.text.upper())])
            print("Цена на " + names[fast_name.index(message.text.upper())] + "(" + fast_name[fast_name.index(message.text.upper())] +")" + " = " + price[fast_name.index(message.text.upper())])
            price.clear()
        elif message.text.upper() in fast_name == False or message.text.upper() != "ПРИВЕТ":
            bot.send_message(message.from_user.id, "Данная валюта не найдена, возможно, ошибка в написании")
            print("Error")

        if message.text == 'list':
            bot.send_message(message.from_user.id, "Список всех валют:\n" + str(list_mass))

    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    main()