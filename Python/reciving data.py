from Python import LogisticRegressionImplement
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import json



app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.after_request
def after_request(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


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
    if usr:
        return "Accepted"
    return {"hi": "bye"}


@app.route("/logisticRegression", methods=["POST"])
def logisticRegression():
    data = request.json  # This is likely a list

    if data:
        try:
            # df = pd.DataFrame(data)  # Convert list to DataFrame
            # csvRaisin = df.to_csv(index=False)  # Convert DataFrame to CSV
            # print(csvRaisin)
            # print(type(csvRaisin))
            with open("data.json","w") as file:
                json.dump(data, file)

            accuracy, Y_true_positive, Y_true_negative, Y_false_positive, Y_false_negative, loss = LogisticRegressionImplement.get_values()

            return jsonify({"Accuracy": accuracy,
                            "Y_predictions": {
                                "Y_true_positive": Y_true_positive,
                                "Y_true_negative": Y_true_negative,
                                "Y_false_positive": Y_false_positive,
                                "Y_false_negative": Y_false_negative
                            },
                            "loss": loss
                            })
        except Exception as e:
            return jsonify({"Error": str(e)})

    return jsonify({"Error": "Failed"})



if __name__ == "__main__":
    app.run(debug=True, host='192.168.165.55', port=5000)


