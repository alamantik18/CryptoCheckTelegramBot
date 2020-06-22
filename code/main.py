import telebot
import constants 
import yobit
import symbols

def main():
    bot=telebot.TeleBot(constants.token)
    mass = symbols.parse()
    mass = [element.lower() for element in mass]
    print(mass)
    @bot.message_handler(commands=['start'])
    def handler_start(message):
        user_markup=telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('btc', 'eth')
        user_markup.row('etc', 'xrp')
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
                        "список всех возможных валют: " + str(mass))

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == 'Привет':
            bot.send_message(message.from_user.id,
                             'Да да, я тут.')
        for element in mass:
            if message.text == element:
                bot.send_message(message.from_user.id,
                                 "Цена на {} = ".format(element) + yobit.get_price(element))

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()