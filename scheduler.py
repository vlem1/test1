import urllib.request
from urllib.error import HTTPError
from time import strftime, time
import asyncio
import httpx
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduler.cache import Cache

'''
def benchmark(func):
    async def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        end = time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return await return_value
    return wrapper
'''

try:
    import asyncio
except ImportError:
    import trollius as asyncio


async def request_url(url: str, url_list: list):
    async with httpx.AsyncClient() as client:
        start_ = time()
        try:
            response = await client.get(url)
            print(f'{url_list.index(url) + 1} ' +
                  url + " Code = " + str(response.status_code) + "\n-----" + str(time()-start_))
        except HTTPError as e:
            print(f'{url_list.index(url) + 1} ' +
                  url + " Error occured! " + "\n-----" + str(time()-start_) + "\n" + str(e))


async def queue():
    tasks = []
    url_list = ['https://www.youtube.com',
                'https://vk.com',
                'https://pythonru.com',
                'https://www.speedtest.net',
                'https://www.icloud.com',
                'https://www.twitch.tv',
                'https://hd.kinopoisk.ru',
                'https://stackoverflow.com',
                'https://www.aviasales.ru',
                'https://hookahplace.ru',
                ]
    for url in url_list:
        tasks.append(asyncio.create_task(request_url(url, url_list)))
    await asyncio.gather(*tasks)


scheduler = AsyncIOScheduler()
# scheduler.add_job(queue, 'interval', seconds=4)
scheduler.add_job(Cache, 'interval', seconds=10)
# TODO: добавить еще одну задачу в планировщик
scheduler.start()
try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    pass

