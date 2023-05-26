from dotenv import load_dotenv
import os

load_dotenv()

PG_USER = os.environ.get('PG_USER')
PG_PASS = os.environ.get('PG_PASS')
PG_HOST = os.environ.get('PG_HOST')
PG_PORT = os.environ.get('PG_PORT')
PG_DB_NAME = os.environ.get('PG_DB_NAME')



