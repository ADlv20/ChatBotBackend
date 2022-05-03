from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    data = {
        "modules": 15,
        "subject": "Data Structures and Algorithms",
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
