from flask import Flask, jsonify, request

app = Flask(__name__)

# List of licensed IPs
LICENSED_IPS = [
    "192.168.0.67",  # Replace this with the actual licensed IPs
    "2402:3a80:1fd2:b3c7:3567:86ca:769e:15f5", 
    # Add more IPs as needed
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
