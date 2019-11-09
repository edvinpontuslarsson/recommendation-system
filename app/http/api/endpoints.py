from flask import Flask, json, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TODO: perhaps send static file from "/"
# app = Flask(__name__, static_folder="../client/build")
# https://stackoverflow.com/questions/44209978/serving-a-create-react-app-with-flask


@app.route("/api", methods=["GET"])
def index():
    response_obj = {"message": "Hello, what is your name?"}
    return json_response(response_obj)


@app.route("/api", methods=["POST"])
def sayHello():
    pass  # TODO: say hello to name


def json_response(payload, status=200):
    # the source code for this function is taken from this tutorial:
    # https://dev.to/oktadev/build-a-simple-crud-app-with-python-flask-and-react-30k5

    return (json.dumps(payload), status, {"content-type": "application/json"})
