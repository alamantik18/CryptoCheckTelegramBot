import telebot
import constants
import symbols

def main():
    bot=telebot.TeleBot(constants.token)
    mass = symbols.parse()
    names = mass[::3]
    fast_name = mass[1::3]
    price = mass[2::3]
    #fast_name = [element.lower() for element in fast_name]
    print(mass)
    print(fast_name)

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
        bot.send_message(message.from_user.id,
                        "Cписок всех возможных валют: " + str(mass[1::3]))

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == 'Привет':
            bot.send_message(message.from_user.id,
                             'Да да, я тут.')
        for i in range(0, len(fast_name), 1):
            if message.text == fast_name[i]:
                bot.send_message(message.from_user.id, "Цена на " + names[i] + "(" + fast_name[i] +") " + " = " + price[i])

        if message.text == 'list':
            bot.send_message(message.from_user.id, "Список всех возможных валют: " + str(mass[1::3]))

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()