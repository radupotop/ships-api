from flask import Flask, Response, abort, jsonify, logging, render_template

from model import Positions, Ships, db
from schema import PositionsSchema, ShipsSchema

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ships/')
def ships():
    result = Ships.select()
    schema = ShipsSchema(many=True)
    return jsonify(schema.dump(result).data)


@app.route('/api/positions/<imo>')
def positions(imo):
    result = (
        Positions.select()
        .where(Positions.imo == imo)
        .order_by(Positions.timestamp.desc())
    )
    if not result:
        return jsonify([]), 404
    schema = PositionsSchema(many=True)
    return jsonify(schema.dump(result).data)


if __name__ == '__main__':
    # The server needs to listen on ANY address for Docker to bind properly
    app.run(debug=True, port=8000, host='0.0.0.0')
