from flask import Flask, jsonify, request

app = Flask(__name__)

# List of licensed IPs
LICENSED_IPS = [
    "114.31.137.25",  # Replace this with the actual licensed IPs
    "203.0.113.5",    # Add more IPs as needed
]

@app.route('/check_ip', methods=['GET'])
def check_ip():
    public_ip = request.remote_addr  # Get client's IP
    if public_ip in LICENSED_IPS:
        return jsonify({"status": "success", "message": "IP is licensed."}), 200
    else:
        return jsonify({"status": "failure", "message": "IP not licensed."}), 403

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
