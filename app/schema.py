from marshmallow import Schema, fields


class ShipsSchema(Schema):
    imo = fields.Int()
    timestamp = fields.DateTime()
    latitude = fields.Float()
    longitude = fields.Float()
