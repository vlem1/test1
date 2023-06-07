import json
import redis
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config import *
from components.projects import crud
from db import get_db
from components.projects.crud import get_project_list


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


class Cache:
    def __init__(self):
        self.client = redis.Redis(host=f'{REDIS_HOST}', port=f'{REDIS_PORT}', decode_responses=True)
        self.set_cache_projects()
        '''
        self.time_cash()
        self.time_list()
        '''

    def set_cache_projects(self):
        db_projects = crud.get_project_list()
        table_projects = {}
        for index in range(len(db_projects)):
            table_projects[db_projects[index].description] = {
                'id': db_projects[index].id,
                'name': db_projects[index].name,
                'description': db_projects[index].description,
                'idAutor': db_projects[index].idAutor,
                'createData': db_projects[index].createData,
                # 'сanDeactivate': db_sensors[index].сanDeactivate,
            }
        table_json = json.dumps(table_projects, indent=4, sort_keys=True, default=str)
        self.client.set('projects', table_json)
        projects_list = Cache.get_cache(self, 'projects')
        print(projects_list)

    def get_cache(self, key: str):
        return_data = self.client.get(key)
        encoded_data = return_data.encode('utf-8')
        return json.loads(encoded_data)

'''
    @benchmark
    def time_cash(self):
        print("cash")
        Cache.get_cache(self, 'projects')

    @benchmark
    def time_list(self):
        print("list")
        get_project_list()
'''

cache = Cache()
