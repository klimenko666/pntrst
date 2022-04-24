import telebot, selenium, time, random
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

token = 'token_bot'



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	but1 = types.KeyboardButton("неко")
	but2 = types.KeyboardButton("тян")
	but3 = types.KeyboardButton("милфа")
	but4 = types.KeyboardButton("лоли")


	markup.add(but1, but2)
	markup.add(but3, but4)
	bot.send_message(message.chat.id, "Привет, этот бот отправляет РАНДОМ аниме-картинки\nСоздатель: @aziz_klimenko666", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def pictures(message):
	try:
		text = []
		text.clear()
		options = webdriver.ChromeOptions()
		options.add_experimental_option("excludeSwitches", ["enable-logging"])
		options.add_argument("--headless")
		service = Service(executable_path=ChromeDriverManager().install())
		driver = webdriver.Chrome(service=service, options=options)

		if (message.text == "неко"):
			driver.get("https://pinterest.jp/search/pins/?q=neko")
			msed = bot.send_message(message.chat.id, "Loading")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading .")
			time.sleep(0.5)
			for _ in range(2):
				driver.execute_script("window.scrollTo(1,100000)")	
				imgs = driver.find_elements(By.TAG_NAME, 'img')
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading . .")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading . . .")
			time.sleep(0.5)
			bot.delete_message(chat_id=message.chat.id, message_id=msed.message_id)



			for img in imgs:
				var = img.get_attribute('src')
				text.append(var)

			bot.send_photo(message.chat.id, photo=f"{random.choice(text)}", caption="#Neko")
#______________________________________________________________________________________________________________________________________
		elif (message.text == "тян"):
			driver.get("https://pinterest.jp/search/pins/?q=anime tyan")
			msed = bot.send_message(message.chat.id, "Loading")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading.")
			time.sleep(0.5)
			for _ in range(2):
				driver.execute_script("window.scrollTo(1, 100000)")
				imgs = driver.find_elements(By.TAG_NAME, 'img')
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading. .")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading. . .")
			time.sleep(0.5)
			bot.delete_message(chat_id=message.chat.id, message_id=msed.message_id)


			for img in imgs:
				var = img.get_attribute('src')
				text.append(var)

			bot.send_photo(message.chat.id, photo=f"{random.choice(text)}", caption="#Tyan")
#______________________________________________________________________________________________________________________________________
		elif (message.text == "милфа"):
			driver.get("https://pinterest.jp/search/pins/?q=JoJo")
			msed = bot.send_message(message.chat.id, "Loading")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading.")
			time.sleep(0.5)
			for _ in range(2):
				driver.execute_script("window.scrollTo(1, 100000)")
				imgs = driver.find_elements(By.TAG_NAME, 'img')
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading. .")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading. . .")
			time.sleep(0.5)
			bot.delete_message(chat_id=message.chat.id, message_id=msed.message_id)


			for img in imgs:
				var = img.get_attribute('src')
				text.append(var)

			bot.send_photo(message.chat.id, photo=f"{random.choice(text)}", caption="#Milf")
#______________________________________________________________________________________________________________________________________
		elif (message.text == "лоли"):
			driver.get("https://pinterest.jp/search/pins/?q=loli")
			msed = bot.send_message(message.chat.id, "Loading")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading.")
			time.sleep(0.5)
			for _ in range(2):
				driver.execute_script("window.scrollTo(1, 100000)")
				imgs = driver.find_elements(By.TAG_NAME, 'img')
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading. .")
			time.sleep(0.5)
			bot.edit_message_text(chat_id=message.chat.id, message_id=msed.message_id, text="Loading. . .")
			time.sleep(0.5)
			bot.delete_message(chat_id=message.chat.id, message_id=msed.message_id)


			for img in imgs:
				var = img.get_attribute('src')
				text.append(var)

			bot.send_photo(message.chat.id, photo=f"{random.choice(text)}", caption="#Loli")
		else:
			bot.send_message(message.chat.id, "Прости, я не понял твоей команды")
	except Exception as e:
		print(e)







if __name__ == '__main__':
	print("STARTED")
	bot.infinity_polling()