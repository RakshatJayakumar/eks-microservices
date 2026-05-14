from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"service": "flask-app", "status": "healthy", "version": "1.0.0"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/data")
def data():
    worker_url = os.environ.get("WORKER_URL", "http://worker-service:5001")
    try:
        response = requests.get(f"{worker_url}/process", timeout=3)
        worker_data = response.json()
    except Exception as e:
        worker_data = {"error": str(e)}

    return jsonify({"source": "flask-app", "worker_response": worker_data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
