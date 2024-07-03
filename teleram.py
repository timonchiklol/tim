import telebot
from config import tokent


bot = telebot.TeleBot(tokent)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Please type any command below to the chat:             1 Mem,  2 Mem sad,  3 Hi how are you,  4 You tomato,  5 Mem eng,  6 Mem lol, 6 Mem kek, 7 Привет, 8 Как дела.")


@bot.message_handler(content_types=['text'])
def new_message(message):
    if message.text == "Mem sad":
        bot.send_photo(message.chat.id, photo="https://12-kanal.ru/vote/habi-lejm-mem-4.jpg")
    elif message.text == "Mem kek":
        bot.send_photo(message.chat.id,
                       photo="https://avatars.dzeninfra.ru/get-zen_doc/1908497/pub_5e667f9c15e73325d76336cb_5e6680aa6c3f9e70e906457f/scale_1200")
    elif message.text == "Mem lol":
        bot.send_photo(message.chat.id, photo="https://i.pinimg.com/474x/88/aa/02/88aa0232b4e2ee1b9d72bf1c6a056a9a.jpg")
    elif message.text == "Mem eng":
        bot.send_photo(message.chat.id, photo="https://www.meme-arsenal.com/memes/8f5adf3103baecffb35bd3e7987070d2.jpg")
    elif message.text == "mem eng":
        bot.send_photo(message.chat.id, photo="https://www.meme-arsenal.com/memes/8f5adf3103baecffb35bd3e7987070d2.jpg")


    elif message.text == "mem kek":
        bot.send_photo(message.chat.id,
                       photo="https://avatars.dzeninfra.ru/get-zen_doc/1908497/pub_5e667f9c15e73325d76336cb_5e6680aa6c3f9e70e906457f/scale_1200")
    elif message.text == "mem sad":
        bot.send_photo(message.chat.id, photo="https://12-kanal.ru/vote/habi-lejm-mem-4.jpg")

    elif message.text == "hi how are you":
        bot.send_message(message.chat.id, "not bad")

    elif message.text == "You tomato":
        bot.send_message(message.chat.id, "no you!!!")
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "Привет!")
    elif message.text == "Как дела":
        bot.send_message(message.chat.id, "Хорошо!")

    elif message.text == "you tomato":
        bot.send_message(message.chat.id, "no you!!!")

    elif message.text == "Hi how are you":
        bot.send_message(message.chat.id, "not bad")
    elif message.text == "Mem":
        bot.send_photo(message.chat.id,
                       photo="https://backupuusites.hb.bizmrg.com/resize_cache/6096307/d5cb5488396720686a69d0c49ef80752/iblock/d45/d45a96c13aa3585ed2e809753cb0b63d/c8de51edbde3e6b51dad851eab7e45f1.jpg")
    elif message.text == "mem lol":
        bot.send_photo(message.chat.id, photo="https://i.pinimg.com/474x/88/aa/02/88aa0232b4e2ee1b9d72bf1c6a056a9a.jpg")
    elif message.text == "mem":
        bot.send_photo(message.chat.id,
                       photo="https://backupuusites.hb.bizmrg.com/resize_cache/6096307/d5cb5488396720686a69d0c49ef80752/iblock/d45/d45a96c13aa3585ed2e809753cb0b63d/c8de51edbde3e6b51dad851eab7e45f1.jpg")
    else:
        bot.send_message(message.chat.id, "sorry i am not tomato")

        pass


bot.polling(none_stop=True)