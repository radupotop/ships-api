import csv

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import config
from model import Positions, Ships, db


def create_db():
    """
    Create DB with psycopg2 since peewee does not support db creation.
    """
    con = connect(host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASS)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute('CREATE DATABASE {}'.format(config.DB_NAME))
    cur.close()
    con.close()


def create_tables():
    """
    Create tables with peewee.
    """
    db.connect()
    db.create_tables((Ships, Positions))


def import_csv_ships():
    with open('../setup/ships.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Ships.create(name=row[0], imo=row[1])


def import_csv_positions():
    with open('../setup/positions.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Positions.create(
                    imo=row[0], timestamp=row[1], latitude=row[2], longitude=row[3]
                )


create_db()
create_tables()
import_csv_ships()
import_csv_positions()
