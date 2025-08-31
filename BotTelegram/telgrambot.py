import telebot
from telebot import types
import time
import config
from animelist import anilist
import random
from random import choice
class BOT:
    def __init__(self, token=config.TOKEN):
        self.bot = telebot.TeleBot(token)
        
        @self.bot.message_handler(commands=['start',"mainmenu"])
        def message_mainmenu(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            but = types.KeyboardButton("Что посмотреть?")
            but2 = types.KeyboardButton('Игры')
            markup.add(but,but2)
            self.bot.send_message(message.chat.id, "Привет, {0.first_name}!Выбирай, что нужно сделать:".format(message.from_user), reply_markup=markup)
            


        @self.bot.message_handler(content_types=["text"])
        def message_messages(message):
            if message.text == "Игры":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                bbut = types.KeyboardButton("/mainmenu")
                butdice = types.KeyboardButton('Бросить кубик')
                butcoin = types.KeyboardButton('Орёл или решка')
               
                markup.add(bbut,butdice,butcoin)
                self.bot.reply_to(message,'Во что играем?', reply_markup=markup)

            elif message.text =='Бросить кубик':                   
                msg = self.bot.send_message(message.chat.id,'Бросаю кубик')
                time.sleep(1)
                for i in range(3):
                    self.bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = "Бросаю кубик.") 
                    time.sleep(1)
                    self.bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = "Бросаю кубик..")
                    time.sleep(1)
                    self.bot.edit_message_text(chat_id = message.chat.id, message_id = msg.message_id, text = "Бросаю кубик...")
                                            
                time.sleep(2)
                tochtovipalo = random.randint(1,6)
                self.bot.reply_to(message,f'Вам выпадает... {tochtovipalo}!')
            
            elif message.text =="Орёл или решка":

                coin = choice(["ОРЕЛ", "РЕШКА"])
                time.sleep(2)
                self.bot.reply_to(message,f'Вам выпадает... {coin}!')

        
            elif message.text =='Что посмотреть?':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                backb = types.KeyboardButton("/mainmenu")
                anm = random.choice(anilist)
                time.sleep(0.5)
                markup.add(backb)
                self.bot.reply_to(message,f'Предлагаю тебе посмотреть: {anm}',reply_markup=markup)
                
        
        
                
    def run(self):
        self.bot.infinity_polling()

if __name__ == '__main__':
    botik = BOT()
    botik.run()
