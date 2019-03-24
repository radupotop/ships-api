from model import db, Ships
import csv


def build_db():
    db.connect()
    db.create_tables((Ships,))


def import_csv():
    with open('../positions.csv') as f:
        reader = csv.reader(f)
        with db.atomic():
            for row in reader:
                Ships.create(
                    imo=row[0], timestamp=row[1], latitude=row[2], longitude=row[3]
                )


build_db()
import_csv()
