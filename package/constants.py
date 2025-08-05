from configparser import ConfigParser
from pathlib import Path

CONFIG_NAME = "config.ini"
CONFIG_PATH = Path(__file__).resolve().parent.parent / CONFIG_NAME

config = ConfigParser()
config.read(CONFIG_PATH)

API_KEY = config['secrets']['api_key']
DATABASE_ID = config['databases']['database_id']

