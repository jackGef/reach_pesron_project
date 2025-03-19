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
    app.run(debug=True, port=8080)