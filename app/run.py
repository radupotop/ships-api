from flask import Flask, abort, jsonify, Response, logging

from webargs import fields
from webargs.flaskparser import use_args

from model import db, Ships
from schema import ShipsSchema

app = Flask(__name__)


@app.route('/api/ships/')
def ships():
    result = Ships.select()
    schema = ShipsSchema(many=True)
    return jsonify({'result': schema.dump(result).data})


@app.route('/api/positions/<imo>')
def positions(imo):
    result = Ships.select().where(Ships.imo == imo).order_by(Ships.timestamp.desc())
    schema = ShipsSchema(many=True)
    return jsonify({'result': schema.dump(result).data})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
