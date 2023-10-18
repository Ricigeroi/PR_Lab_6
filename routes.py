from flask import request, jsonify
from models.electro_scooter import ElectroScooter
from __main__ import app


@app.route('/api/electro-scooters', methods=['POST'])
def create_electro_scooter():
    try:
        data = request.get_json()
        name = data['name']
        battery_level = data['battery_level']
        electro_scooter = ElectroScooter.create(name, battery_level)
        return jsonify({"message": "Electro Scooter created successfully"}), 201
    except KeyError:
        return jsonify({"error": "Invalid request data"}), 400


@app.route('/api/electro-scooters/<int:scooter_id>', methods=['GET'])
def get_electro_scooter_by_id(scooter_id):
    scooter = ElectroScooter.get_by_id(scooter_id)
    if scooter:
        return jsonify({
            "id": scooter.id,
            "name": scooter.name,
            "battery_level": scooter.battery_level
        }), 200
    else:
        return jsonify({"error": "Electro Scooter not found"}), 404


@app.route('/api/electro-scooters/<int:scooter_id>', methods=['PUT'])
def update_electro_scooter(scooter_id):
    scooter = ElectroScooter.get_by_id(scooter_id)
    if scooter:
        data = request.get_json()
        scooter.name = data.get('name', scooter.name)
        scooter.battery_level = data.get('battery_level', scooter.battery_level)
        scooter.update()
        return jsonify({"message": "Electro Scooter updated successfully"}), 200
    else:
        return jsonify({"error": "Electro Scooter not found"}), 404


@app.route('/api/electro-scooters/<int:scooter_id>', methods=['DELETE'])
def delete_electro_scooter(scooter_id):
    scooter = ElectroScooter.get_by_id(scooter_id)
    if scooter:
        # Get the password from the request headers
        password = request.headers.get('X-Delete-Password')
        if password == '123':
            scooter.delete()
            return jsonify({"message": "Electro Scooter deleted successfully"}), 200
        else:
            return jsonify({"error": "Incorrect password"}), 401
    else:
        return jsonify({"error": "Electro Scooter not found"}), 404
