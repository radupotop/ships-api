from model import db, Ships, Positions
import csv


def build_db():
    db.connect()
    db.create_tables((Ships, Positions))


def import_csv_ships():
    with open('../ships.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Ships.create(name=row[0], imo=row[1])


def import_csv_positions():
    with open('../positions.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Positions.create(
                    imo=row[0], timestamp=row[1], latitude=row[2], longitude=row[3]
                )


build_db()
import_csv_ships()
import_csv_positions()
