from flask import Flask,jsonify,request
from models.pow_model import calculate_power



def pow_function():
    data = request.get_json()
    number = data.get('number')
    power= data.get('power')

    if number is None or power is None:
        return jsonify({"error": "Missing number or power"}),400

    number_pow = calculate_power(number,power)
    return jsonify({"number": number,
                    "power": power,
                    "number_pow": number_pow})