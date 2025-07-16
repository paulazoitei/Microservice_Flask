from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/pow_function", methods=['POST'])
def calculate_pow():
    data = request.get_json()
    number = data.get('number')
    power= data.get('power')
    number_pow=number**power
    return jsonify({"number": number,
                    "power": power,
                    "number_pow":number_pow})



if __name__=="__main__":
    app.run(port=8081)