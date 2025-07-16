from flask import Flask

from controllers.n_th_fibonacci_controller import fibo_function
from controllers.pow_controller import  pow_function
from controllers.factorial_controller import factorial_function


app = Flask(__name__)
app.add_url_rule('/pow_function', view_func=pow_function, methods=['POST'])
app.add_url_rule('/fibo_function', view_func=fibo_function,methods=['POST'])
app.add_url_rule('/factorial_function',view_func=factorial_function, methods=['POST'])

if __name__=="__main__":
    app.run(port=8081)

