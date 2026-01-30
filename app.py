from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis (Host will be 'redis' in K8s/Docker)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('hits')
    return jsonify({
        "message": "Hello from Kubernetes!\nWith additional Line",
        "visits": count,
        "hostname": os.getenv("HOSTNAME")
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
