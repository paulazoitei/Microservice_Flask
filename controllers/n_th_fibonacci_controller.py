from flask import Flask,jsonify,request
from services.n_th_fibonacci_service import FibonacciService

class FibonacciController:
    def fibo_function(self):
        data=request.get_json()
        n=data.get('n')

        if n is None :
            return jsonify({"error":"Missing argument"}),400
        service=FibonacciService()
        result=service.fibo(n)
        return jsonify({
            "n_th_term":n,
            "result":result
        })