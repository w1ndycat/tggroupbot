import telepot
import pprint
import time
import requests


# 获取并发布色图

def setu_today():
    r = requests.request('get', 'https://lolisuki.cc/api/setu/v1?level=4-6&tag=萝莉|白丝')
    setu_r = r.json()
    pprint.pp(setu_r)
    bot.sendMessage(-1001699752977, '今日份色图,可以开冲啦！😍')
    # setu_pto = setu_r['data']['urls']['regular']
    bot.sendPhoto(-1001699752977, str(setu_r['data']['urls']['regular']))


bot = telepot.Bot('5353640625:AAFzT24U4B3EiOI-Wxa71N5qM4TzOb1Xsdw')

localtime = time.localtime(time.time())
day_now = 0
while True:
    if day_now != localtime[2] and localtime[3] == 13:
        day_now = localtime
        setu_today()
