from flask import Flask, json, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api", methods=["GET"])
def get_api_index():
    response_obj = {"message": "Hello, what is your name?"}
    return json_response(response_obj)


@app.route("/api", methods=["POST"])
def post_api_index():
    data = request.get_json()
    name = data["name"]

    response_obj = {"message": "Hello " + name}
    return json_response(response_obj)


def json_response(payload, status=200):
    # the source code for this function is taken from this tutorial:
    # https://dev.to/oktadev/build-a-simple-crud-app-with-python-flask-and-react-30k5

    return (json.dumps(payload), status, {"content-type": "application/json"})
