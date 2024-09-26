from flask import Flask, request, jsonify

app = Flask(__name__)

# A list of authorized serial numbers (this can be replaced with a database)
AUTHORIZED_SERIALS = ["R6N0CV13K171258", "SERIAL67890", "SERIAL98765"]

@app.route('/check_serial', methods=['POST'])
def check_serial():
    data = request.get_json()

    # Ensure the serial number is provided in the request
    if 'serial_number' not in data:
        return jsonify({"authorized": False, "message": "Serial number not provided"}), 400

    serial_number = data['serial_number']

    # Check if the serial number is in the list of authorized serials
    if serial_number in AUTHORIZED_SERIALS:
        return jsonify({"authorized": True, "message": "Serial number is authorized"}), 200
    else:
        return jsonify({"authorized": False, "message": f"Unauthorized serial number: {serial_number}"}), 403

if __name__ == '__main__':
    app.run(debug=True)
