from model import db, Ships
from config import DB_NAME


def build():
    db.connect()
    db.create_tables((Ships,))


build()
