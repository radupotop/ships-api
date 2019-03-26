from flask import Flask

from api.views import api
from frontend.views import frontend

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(frontend, url_prefix='/')

if __name__ == '__main__':
    # The server needs to listen on ANY address for Docker to bind properly
    app.run(debug=True, port=8000, host='0.0.0.0')
