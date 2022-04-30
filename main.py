import time
import requests
import random
import schedule
import json
from os.path import exists

if not exists('config.json'):
    print('Please create a config.json file.')
    exit(1)

with open('config.json', 'r') as f:
    cfg = json.load(f)


def post_message():
    user_list = random.sample(cfg['users'], len(cfg['users']))
    requests.post('https://slack.com/api/chat.postMessage', {
        'token': cfg['bot_token'],
        'channel': cfg['channel'],
        'text': ', '.join(user_list)
    })


# schedule daily
schedule.every().day.at(cfg['time_of_day']).do(post_message)

while True:
    schedule.run_pending()
    time.sleep(1)
