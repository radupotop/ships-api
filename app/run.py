from flask import Flask, Response, abort, jsonify, logging
from webargs import fields
from webargs.flaskparser import use_args

from model import Positions, Ships, db
from schema import PositionsSchema, ShipsSchema

app = Flask(__name__)


@app.route('/api/ships/')
def ships():
    result = Ships.select()
    schema = ShipsSchema(many=True)
    return jsonify({'result': schema.dump(result).data})


@app.route('/api/positions/<imo>')
def positions(imo):
    result = (
        Positions.select()
        .where(Positions.imo == imo)
        .order_by(Positions.timestamp.desc())
    )
    schema = PositionsSchema(many=True)
    return jsonify({'result': schema.dump(result).data})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
