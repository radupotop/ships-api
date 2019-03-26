import peewee as pw

from db import db


class BaseModel(pw.Model):
    class Meta:
        database = db


class Ships(BaseModel):
    imo = pw.PrimaryKeyField()
    name = pw.CharField()


class Positions(BaseModel):
    imo = pw.ForeignKeyField(Ships, field='imo', backref='positions')
    timestamp = pw.DateTimeField()
    latitude = pw.DoubleField()
    longitude = pw.DoubleField()
