from telebot import types


def start_bot_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd_currency = types.KeyboardButton('💸 USD rate')
    eur_currency = types.KeyboardButton('💶 EUR rate')
    rub_currency = types.KeyboardButton('🪙 RUB rate')
    tenge_currency = types.KeyboardButton('💴 KZT rate')
    frank_currency = types.KeyboardButton('💵 CHF rate')
    pound_currency = types.KeyboardButton('💷 GBP rate')
    yen_currency = types.KeyboardButton('💴 JPY rate')
    markup.row(usd_currency, eur_currency, rub_currency)
    markup.row(tenge_currency, frank_currency, pound_currency)
    markup.add(yen_currency)
    return markup


def remove_buttons():
    return types.ReplyKeyboardRemove()