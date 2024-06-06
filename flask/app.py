from logging import debug
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route("/universities")
def get_universities():
    API_URL = "http://universities.hipolabs.com/search?country="
    search = request.args.get("country")
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
