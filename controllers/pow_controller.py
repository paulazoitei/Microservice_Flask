from flask import Flask,jsonify,request
from services.pow_service import PowService


class PowController:

    def pow_function(self):
        data = request.get_json()
        number = data.get('number')
        power= data.get('power')

        if number is None or power is None:
            return jsonify({"error": "Missing number or power"}),400
        try:
            number = float(number)
            power = float(power)
        except (TypeError, ValueError):
            return jsonify({"error": "Number and power must be numeric"}), 400
        if not power.is_integer():
            return jsonify({"error": "Power must be an integer"}), 400
        if number == 0 and power < 0:
            return jsonify({"error": "Cannot raise 0 to a negative power"}), 400

        if number < 0 and not power.is_integer():
            return jsonify({"error": "Negative base with fractional power is not allowed"}), 400

        service=PowService()
        number_pow = service.calculate_power(number,power)
        return jsonify({"number": number,
                        "power": power,
                        "number_pow": number_pow})