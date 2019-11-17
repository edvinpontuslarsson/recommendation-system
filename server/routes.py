from flask import Flask, json, request
from flask_cors import CORS
import data_access_layer
import recommendations

app = Flask(__name__)
CORS(app)


@app.route("/api", methods=["GET"])
def get_api_index():
    response_obj = {"message": "Welcome to the API"}
    return json_response(response_obj)


@app.route("/api/recommendations/euclidean/<id>")
def get_euclidean(id):
    all_data = data_access_layer.get_all_data()
    euclideans = recommendations.get_euclideans(id, all_data)
    return json_response(euclideans)


def json_response(payload, status=200):
    # the source code for this function is taken from this tutorial:
    # https://dev.to/oktadev/build-a-simple-crud-app-with-python-flask-and-react-30k5

    return (json.dumps(payload), status, {"content-type": "application/json"})
