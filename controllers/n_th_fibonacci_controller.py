from flask import Flask,jsonify,request
from models.n_th_fibonacci_model import fibo


def fibo_function():
    data=request.get_json()
    n=data.get('n')

    if n is None :
        return jsonify({"error":"Missing argument"}),400
    result=fibo(n)
    return jsonify({
        "n_th_term":n,
        "result":result
    })