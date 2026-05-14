from flask import Flask, jsonify
import random
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"service": "worker-service", "status": "healthy"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/process")
def process():
    return jsonify(
        {
            "processed": True,
            "result": random.randint(1, 1000),
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "worker": "worker-service-v1",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
