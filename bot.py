import telebot
from telebot import types
import requests

Kabos = telebot.TeleBot('2081681159:AAH9oLMkopPxih8rP4P5Nx9H8JeSX4rFWE4')#ToKeN

@Kabos.message_handler(commands=['start'])
def starh(message):
	Kabos.send_message(message.chat.id, text=' - hi in bot, date account instagram ðŸ‘€ðŸ”±\n- send user?\n--------\n- programmerÂ² : @nnkonn-@tzzzz')
@Kabos.message_handler(func=lambda m: True)	
def kabos(message):
	kaQ = message.text
	kaS = (f'https://tzzzzava.xyz/Apis/kabos/date-insta.php?user={kaQ}')
	req = requests.get(kaS)
	kaz = req.json()
	kan = kaz['result']
	Kaop = f' â€¢ Date Account : {kan} .'
	Kabos.send_message(message.chat.id,Kaop)
	
Kabos.polling(True)	