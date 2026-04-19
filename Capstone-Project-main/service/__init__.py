from flask import Flask, jsonify
from flask_talisman import Talisman
from flask_cors import CORS

def create_app():

    app = Flask(__name__)

    talisman = Talisman(app)
    talisman.force_https = False

    CORS(app)

    @app.route("/")
    def index():
        return jsonify({"message": "Customer Accounts Microservice Running"})

    return app

app = create_app()