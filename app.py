from flask import Flask, jsonify, request

app = Flask(__name__)

# List of licensed IPs
LICENSED_IPS = [
    "192.168.0.67", 
    '112.196.47.98',# Replace this with the actual licensed IPs new era ip
    '192.168.1.10'
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
