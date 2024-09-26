from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

LICENSED_IP = " 2402:3a80:1fd4:d4c7:fd95:f0c6:7602:781d"  # Replace this with the actual licensed IP

@app.route('/check_ip', methods=['GET'])
def check_ip():
    public_ip = request.remote_addr  # Get client's IP
    if public_ip == LICENSED_IP:
        return jsonify({"status": "success", "message": "IP is licensed."}), 200
    else:
        return jsonify({"status": "failure", "message": "IP not licensed."}), 403

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
