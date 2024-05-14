import time
import requests
import random
import schedule
import json
from os.path import exists
from functools import partial

if not exists('config.json'):
    print('Please create a config.json file.')
    exit(1)

with open('config.json', 'r') as f:
    cfg = json.load(f)


def post_message(_day):
    users = [u for u in cfg['users'] if u not in _day.get('excluded', [])]
    requests.post('https://slack.com/api/chat.postMessage', {
        'token': cfg['bot_token'],
        'channel': cfg['channel'],
        'text': ', '.join(random.sample(users, len(users)))
    })


day_lookup = {
    'mon': schedule.every().monday,
    'tue': schedule.every().tuesday,
    'wed': schedule.every().wednesday,
    'thu': schedule.every().thursday,
    'fri': schedule.every().friday,
    'sat': schedule.every().saturday,
    'sun': schedule.every().sunday,
}

# create schedule from config
for day, schedule in cfg['schedules']:
    print(f'scheduled posting for {day} at {schedule["time_of_day"]}')
    day_lookup[day].at(schedule['time_of_day']).do(partial(post_message, schedule))

while True:
    schedule.run_pending()
    time.sleep(1)
