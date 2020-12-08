import os
import requests
import redis
import time

r = redis.from_url(os.get.envrion("REDIS_URL"))

# r = redis.from_url("YOUR_REDIS_DB_URL")

db_keys = r.keys(pattern="*")
bot_token = '1471191637:AAFIErz34R7SB4bW3_CONraCGhpyJpDtd5c'

def send_announcments(bot_message):
    for keys in db_keys:
        keys_values = r.get(keys).decode("UTF-8")
        print(keys_values)
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + keys_values + '&text=' + bot_message
        print(send_text)
        response = requests.get(send_text)
        print (response.json())
        time.sleep(1)

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

bot_message = open (os.path.join(__location__, "message_bot.txt"))

text_content = bot_message.read()

send_announcments(bot_message = text_content)