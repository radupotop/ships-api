from flask import Blueprint, abort, jsonify, logging

from .model import Positions, Ships, db
from .schema import PositionsSchema, ShipsSchema

api = Blueprint('api', __name__)


@api.route('/ships/')
def ships():
    result = Ships.select()
    schema = ShipsSchema(many=True)
    return jsonify(schema.dump(result).data)


@api.route('/positions/<int:imo>')
def positions(imo):
    result = (
        Positions.select()
        .where(Positions.imo == imo)
        .order_by(Positions.timestamp.desc())
    )
    if not result:
        return abort(404)

    schema = PositionsSchema(many=True)
    return jsonify(schema.dump(result).data)


@api.errorhandler(404)
def page_not_found(e):
    return jsonify('Not Found'), 404
