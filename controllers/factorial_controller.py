from flask import Flask,jsonify,request
from models.factorial_model import factorial


def factorial_function():
    data= request.get_json()
    number =data.get('number')

    if number is None:
        return jsonify({"error":"Missing argument"}),400

    result=factorial(number)

    return jsonify({
        "number":number,
        "result":result
    })