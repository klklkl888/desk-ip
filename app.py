from flask import Flask, jsonify, request

app = Flask(__name__)

# List of licensed IPs
LICENSED_IPS = [
    "192.168.202.48",  # Replace this with the actual licensed IPs
    "2402:3a80:1fd2:b3c7:3567:86ca:769e:15f5",  # Add more IPs as needed
    "127.0.0.1",
]

@app.route('/check_ip', methods=['GET'])
def check_ip():
    public_ip = request.remote_addr  # Get client's IP
    print(f"Retrieved IP: {public_ip}")  # Debug: Print the IP address
    if public_ip in LICENSED_IPS:
        return jsonify({
            "status": "success",
            "message": "IP is licensed.",
            "ip": public_ip
        }), 200
    else:
        return jsonify({
            "status": "failure",
            "message": "IP not licensed.",
            "ip": public_ip
        }), 403

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
