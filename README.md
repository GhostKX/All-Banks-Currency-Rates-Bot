# 🏦 All Banks Currency Rates Bot  

A **Python-based Telegram bot** that provides real-time exchange rates from **multiple banks in Uzbekistan**. Users can check exchange rates for various currencies, compare rates across banks, and receive an image-based summary of the latest rates.  

Built using **PyTelegramBotAPI**, **Selenium**, and **BeautifulSoup**, this bot ensures accurate and up-to-date currency exchange information.  

---

## Features  

### 📈 Exchange Rates  
- **Live Rates from Multiple Banks**  
- **Compare Buy & Sell Prices** across banks  
- **Supports Multiple Currencies**  
- **Image-Based Rate Summary** for better visualization  
- **Daily Rate Updates**  

### 💸 Supported Currencies  
- 🇺🇸 **USD** (US Dollar)  
- 🇪🇺 **EUR** (Euro)  
- 🇷🇺 **RUB** (Russian Ruble)  
- 🇰🇿 **KZT** (Kazakhstani Tenge)  
- 🇨🇭 **CHF** (Swiss Franc)  
- 🇬🇧 **GBP** (British Pound)  
- 🇯🇵 **JPY** (Japanese Yen)  

### User-Friendly Interface  
- **Interactive Telegram Buttons** for navigation  
- **Image-Based Reports**  
- **Error Handling & Smooth User Flow**  

---

## Requirements  

- **Python 3.x**  
- **Google Chrome & Chrome WebDriver**  
- **Libraries:**  
  - `telebot` (Telegram API)  
  - `selenium` (Web Scraping)  
  - `beautifulsoup4` (HTML Parsing)  
  - `Pillow` (Image Processing)  
  - `dotenv` (Environment Variables)  
  - `webdriver-manager` (ChromeDriver Management)  

---

## Installation  

1. Clone the Repository  
```bash
git clone https://github.com/GhostKX/All-Banks-Currency-Rates-Bot.git
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Configure the bot

- Create a .env file to store your Telegram API Key and OpenWeatherMap API Key
- Add your Telegram Bot Token:

```
API_KEY=your-telegram-bot-token
```

4. Navigate to the project directory
```bash
cd All-Banks-Currency-Rates-Bot
```

5. Run the bot
```bash
python PythonAllBanksCurrencies_bot.py
```

---

## Usage  

### Initial Setup  
- Start the bot by sending `/start` in Telegram.  
- Choose an option:  
   - 💸 **USD Rate** (US Dollar)  
   - 💶 **EUR Rate** (Euro)  
   - 🪙 **RUB Rate** (Russian Ruble)  
   - 💴 **KZT Rate** (Kazakhstani Tenge)  
   - 💵 **CHF Rate** (Swiss Franc)  
   - 💷 **GBP Rate** (British Pound)  
   - 💴 **JPY Rate** (Japanese Yen)  

### Getting Exchange Rates  
- **Select a currency**   
- The bot will **scrape the latest exchange rates** from Uzbekistan banks
- The result will be sent as an **image** containing the exchange rates  

### Example Output:  

```
🏦 USD Exchange Rates  

📅 15 February 2025  
______________________________  
🏛️ Bank A | Buy: 12,500 | Sell: 12,700  
🏛️ Bank B | Buy: 12,450 | Sell: 12,750  
🏛️ Bank C | Buy: 12,480 | Sell: 12,720  
______________________________  
```

---

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/All-Banks-Currency-Rates-Bot)**