# All Banks Currencies Bot

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import telebot
from bs4 import BeautifulSoup

import buttons
import time

from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()
API_KEY = str(os.getenv('API_KEY'))
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start_bot(message):
    user_id = message.from_user.id
    bot.send_message(user_id, '🏦 Welcome to the currency exchange rate bot in all banks 🏦',
                     reply_markup=buttons.start_bot_buttons())
    bot.register_next_step_handler(message, currency_type)


def currency_type(message):
    user_id = message.from_user.id
    if message.text == '💸 USD rate':
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        dollar_in_the_office = 'Доллары (офис)'
        image_name = 'images/dollar_image.png'
        header = "$ USD (dollar) Exchange Rates"
        generated_image = f'{user_id}_banks_currency_rates.png'
        from_top_get = 32
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    elif message.text == '💶 EUR rate':
        dollar_in_the_office = 'Евро'
        image_name = 'images/euro_image.png'
        header = "€ EUR (euro) Exchange Rates"
        generated_image = f'{user_id}_euro_banks_currency_rates.png'
        from_top_get = 33
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    elif message.text == '🪙 RUB rate':
        dollar_in_the_office = 'Рубли'
        image_name = 'images/ruble_image.png'
        header = "₽ RUB (ruble) Exchange Rates"
        generated_image = f'{user_id}_ruble_banks_currency_rates.png'
        from_top_get = 35
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    elif message.text == '💴 KZT rate':
        dollar_in_the_office = 'Тенге'
        image_name = 'images/tenge_image.png'
        header = "₸ KZT (tenge) Exchange Rates"
        generated_image = f'{user_id}_tenge_banks_currency_rates.png'
        from_top_get = 40
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    elif message.text == '💵 CHF rate':
        dollar_in_the_office = 'Франк'
        image_name = 'images/frank_image.png'
        header = "₣ CHF (frank) Exchange Rates"
        generated_image = f'{user_id}_frank_banks_currency_rates.png'
        from_top_get = 40
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    elif message.text == '💷 GBP rate':
        dollar_in_the_office = 'Фунт'
        image_name = 'images/pound_image.png'
        header = "£ GBP (pound) Exchange Rates"
        generated_image = f'{user_id}_pound_banks_currency_rates.png'
        from_top_get = 40
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    elif message.text == '💴 JPY rate':
        dollar_in_the_office = 'Иена'
        image_name = 'images/yen_image.png'
        header = "￥ JPY (yen) Exchange Rates"
        generated_image = f'{user_id}_yen_banks_currency_rates.png'
        from_top_get = 40
        bot.send_message(user_id, 'Loading data 🔎 ...', reply_markup=buttons.remove_buttons())
        rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get)
    else:
        bot.send_message(user_id, '❌ Error. Invalid symbols ❌'
                                  '\n\n ⬇️ Please use buttons below 💬 ⬇️', reply_markup=buttons.start_bot_buttons())
        bot.register_next_step_handler(message, currency_type)


def rate_show(message, dollar_in_the_office, image_name, header, generated_image, from_top_get):
    user_id = message.from_user.id
    url = 'https://pultop.uz/kurs-obmena-valyut/'

    # Set up Selenium driver using ChromeDriverManager
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('---headless')  # Run Chrome in headless mode (optional)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open the URL
    driver.get(url)

    try:
        dropdown_button = driver.find_element(By.ID, "calc-kurs-currency")
        select = Select(dropdown_button)
        select.select_by_visible_text(f'{dollar_in_the_office}')
        time.sleep(2)
    except Exception as e:
        bot.send_message(user_id, '❌ Error. Could not extract data from website ❌'
                                  '\n\n Please try again later 💬')
        bot.register_next_step_handler(message, currency_type)
        print(f"Error: {e}")

    # Click "Load More" button until all content is loaded
    try:
        show_all_button = driver.find_element(By.XPATH, "//span[@id='showall-kurs']")
        show_all_button.click()
        time.sleep(2)  # Wait for content to load
    except Exception as e:
        bot.send_message(user_id, '❌ Error. Could not extract data from website ❌'
                                  '\n\n Please try again later 💬')
        bot.register_next_step_handler(message, currency_type)
        print(f"Error: {e}")

    # Extract the HTML content after all rows are loaded
    html = driver.page_source
    driver.quit()  # Close the browser

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'id': 'wp_pultop_kurs'})
    tbody_rows = table.find('tbody', {'id': 'kurs_row'}).find_all('tr')

    all_banks = []

    for row in tbody_rows:
        bank_name = row.find('div', {'class': 'name-kurs'}).text.strip()
        buy_price = row.find('td', {'class': 'kurs-table-field1'}).text.replace(' сум', '').strip()
        sell_price = row.find_all('td')[2].text.replace(' сум', '').strip()
        all_banks.append([bank_name, buy_price, sell_price])

    # Format message with aligned columns
    formatted_date = datetime.today().strftime('For %d of %B, %Y')

    background_image = Image.open(f'{image_name}')

    img_with_background = background_image.copy()
    draw = ImageDraw.Draw(img_with_background)

    header_font = ImageFont.truetype("Arial Unicode.ttf", 30)
    font = ImageFont.truetype("Arial Unicode.ttf", 25)

    date = f"{formatted_date}"
    column_name_bank_name = f'Bank Name'
    column_name_buy = 'Buy'
    column_name_sell = 'Sell'
    line = f"{'_' * 51}"

    draw.text((160, 5), header, fill=(255, 255, 255), font=header_font)
    draw.text((220, 40), date, fill=(255, 255, 255), font=font)
    draw.text((20, 78), column_name_bank_name, fill=(255, 255, 255), font=font)
    draw.text((400, 78), column_name_buy, fill=(255, 255, 255), font=font)
    draw.text((600, 78), column_name_sell, fill=(255, 255, 255), font=font)
    draw.text((20, 85), line, fill=(255, 255, 255), font=font)

    from_top = 115
    for bank in all_banks:
        bank_name, buy_price, sell_price = bank
        draw.text((20, from_top), bank_name, fill=(255, 255, 255), font=font)  # White for bank name
        draw.text((400, from_top), buy_price, fill=(255, 255, 255), font=font)
        draw.text((600, from_top), sell_price, fill=(255, 255, 255), font=font)
        from_top += from_top_get

    generated_image = f'generated_images/{generated_image}'

    img_with_background.save(generated_image, format='PNG')

    with open(generated_image, 'rb') as photo:
        bot.send_photo(user_id, photo, reply_markup=buttons.start_bot_buttons())

    os.remove(generated_image)

    bot.register_next_step_handler(message, currency_type)


# Running the bot infinitely
bot.polling(non_stop=True)
