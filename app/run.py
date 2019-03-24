from flask import Flask, abort, jsonify, Response, logging

from webargs import fields
from webargs.flaskparser import use_args

from model import db, Ships
from schema import ShipsSchema

app = Flask(__name__)

index_args = {'imo': fields.Int()}


@app.route('/api/ships/')
@use_args(index_args)
def index(args):
    result = Ships.select()
    schema = ShipsSchema(many=True)
    return jsonify({'result': schema.dump(result).data})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
