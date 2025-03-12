from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route("/api/users", methods=["GET"])
def users():
    return jsonify(
        {
            "users": [
                "jackob",
                "Matan",
                "Logistic regression"
            ]
        }
    )

@app.route("/api/users/jack/<usr>", methods=["GET", "POST"])
def user(usr):
    if usr :
        return "Accepted"
    return {"Nooooo": "Stop ITTTTTTT"}

@app.route("/logisticRegression/<data>", methods=["POST"])
def logisticRegression(data):
    if data:
        return {"Success": "you've the response data"}

    return {"Error": "Failed to get data"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)






















# @app.after_request
# def after_request(response):
#   response.headers.set('Access-Control-Allow-Origin', '*')
#   response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response 