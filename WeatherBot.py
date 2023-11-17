"""
This is a simple weather bot that sends weather updates to users every day at 7:00 am.
"""
import telebot
import requests
import schedule
import time
import threading

"""
The following variables need to be replaced with your own tokens, location and time.
"""
BOT_TOKEN = 'bot_token'
WEATHER_TOKEN = 'weather_token'
bot = telebot.TeleBot(BOT_TOKEN)
latitude = 'my_latitude'
longitude = 'my_longitude'
my_time = 'the_time'
chat_id = set()
empty_set = True
run = False
my_thread = threading.Thread()


@bot.message_handler(commands=['start'])
def start(message):
    """
    this method is called when the user sends '/start' command to the bot.
    it sends a welcome message to the user and adds the user's chat id to the 'chat_id' set.
    if the set was empty, it starts the 'begin_messaging' function in a separate thread.
    """
    global empty_set
    bot.send_message(message.chat.id, 'Hello! I am WeatherBot.\n'
                                      'I will tell you the weather in Milan everyday at 7:00 am. ')
    chat_id.add(message.chat.id)
    if empty_set:
        global run
        global my_thread
        empty_set = False
        run = True
        my_thread = threading.Thread(target=begin_messaging)
        my_thread.start()


def begin_messaging():
    """
    this function is called when the first user is added in the set and starts the scheduler.
    """
    global run
    while run:
        schedule.run_pending()
        time.sleep(1)


def send_forecast():
    """
    this function is called by the scheduler and sends the weather forecast to all the users in the set.
    """
    url = 'https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&exclude{}&appid={}'.format(
        latitude, longitude, 'current,minutely,hourly,alerts', WEATHER_TOKEN)
    weather = requests.get(url).json()
    data = weather['daily']
    data_2 = data[0]
    info = data_2['weather']
    data_3 = info[0]
    main = data_3['main']
    description = data_2['summary']
    temp = data_2['temp']
    temp_max = temp['max'] - 273.15
    temp_min = temp['min'] - 273.15
    t_felt = data_2['feels_like']
    t_felt_day = t_felt['day'] - 273.15
    weather_message = (f'*Weather: {main}*\n{description}\nTemperature max: {temp_max:.2f}°C'
                       f'\nTemperature min: {temp_min:.2f}°C\nFeels like during the day: {t_felt_day:.2f}°C')
    for i in chat_id:
        bot.send_message(i, weather_message, parse_mode='Markdown')


@bot.message_handler(commands=['stop'])
def stop(message):
    """
    this method is called when the user sends '/stop' command to the bot.
    it removes the user's chat id from the 'chat_id' set and sends a message to the user.
    if the set is empty, it stops the scheduler and the thread.
    """
    try:
        chat_id.remove(message.chat.id)
        bot.send_message(message.chat.id, 'You have successfully stopped the weather updates.\n'
                                          'I hope you enjoyed the service.')
        if len(chat_id) == 0:
            global empty_set
            global run
            run = False
            empty_set = True
    except KeyError:
        bot.send_message(message.chat.id, 'You do not have any active session.')


@bot.message_handler(func=lambda msg: True)
def response_all(message):
    """
    this method is called when the user sends a message to the bot.
    """
    bot.reply_to(message, 'Sorry I am not ChatGPT, I am just a weather bot.\n'
                          'I can only tell you the weather, every other message you send me will be ignored.')


"""
The following line of code schedules the 'send_forecast' function to be called everyday at 7:00 am.
"""
schedule.every().day.at(my_time).do(send_forecast)

bot.infinity_polling()
