from flask import Flask,jsonify,request
from services.factorial_service import FactorialService


class FactorialController:
    def factorial_function(self):
        data= request.get_json()
        number =data.get('number')

        if number is None:
            return jsonify({"error":"Missing argument"}),400
        elif not isinstance(number,int):
            return jsonify({"error":"Not int number cannot be calculated"}),400
        elif number <0:
            return jsonify({"error":"Negative number cannot be calculated"}),400

        service=FactorialService()
        result=service.factorial(number)


        return jsonify({
            "number":number,
            "result":result
        })