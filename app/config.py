import os

DB_NAME = 'polestar'
DB_HOST = 'db' if os.getenv('IS_DOCKER') else 'localhost'
DB_USER = 'postgres'
DB_PASS = ''
