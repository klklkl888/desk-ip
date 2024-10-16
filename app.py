from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary of licensed IPs with their associated PC names or locations
LICENSED_IPS = {
    "192.168.202.48": "PC1 - Office",  # Replace with actual IPs and names/locations
    "2402:3a80:1fd2:b3c7:3567:86ca:769e:15f5": "PC2 - Remote",  # Add more IPs with location or name
    '': ''
}

# Dictionary to capture all IP requests along with PC names or locations
ALL_IP_REQUESTS = {}

# List of blocked IPs
BLOCKED_IPS = []

@app.route('/check_ip', methods=['GET'])
def check_ip():
    public_ip = request.remote_addr  # Get client's IP
    
    # Capture the IP making the request along with its PC name or location
    if public_ip not in ALL_IP_REQUESTS:
        pc_name_or_location = LICENSED_IPS.get(public_ip, "Unknown Location")
        ALL_IP_REQUESTS[public_ip] = pc_name_or_location
    
    # Check if the IP is licensed
    if public_ip in LICENSED_IPS:
        return jsonify({"status": "success", "message": f"IP is licensed for {LICENSED_IPS[public_ip]}."}), 200
    else:
        # Add to the blocked IPs list if not already there
        if public_ip not in BLOCKED_IPS:
            BLOCKED_IPS.append(public_ip)
        return jsonify({"status": "failure", "message": "IP not licensed."}), 403

# Route to get the list of licensed IPs that have made requests along with PC names or locations
@app.route('/licensed_ips', methods=['GET'])
def licensed_ips():
    licensed_ip_requests = {ip: pc_name for ip, pc_name in ALL_IP_REQUESTS.items() if ip in LICENSED_IPS}
    return jsonify({"licensed_ips": licensed_ip_requests})

# Route to get the list of blocked IPs
@app.route('/blocked_ips', methods=['GET'])
def blocked_ips():
    return jsonify({"blocked_ips": BLOCKED_IPS})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
