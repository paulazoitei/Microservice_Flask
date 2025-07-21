from flask import Flask,jsonify,request
from services.pow_service import PowService


class PowController:

    def pow_function(self):
        data = request.get_json()
        number = data.get('number')
        power= data.get('power')

        if number is None or power is None:
            return jsonify({"error": "Missing number or power"}),400
        service=PowService()
        number_pow = service.calculate_power(number,power)
        return jsonify({"number": number,
                        "power": power,
                        "number_pow": number_pow})