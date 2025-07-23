from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.n_th_fibonacci_controller import FibonacciController
from controllers.pow_controller import PowController
from controllers.factorial_controller import FactorialController
from repositories.database import  db
import time
from datetime import datetime
from services.request_logging_service import RequestLoggingService
from flask import request
from models.request_log import RequestLog
from controllers.get_all_requests_controller import GetAllRequestsController
import flask_monitoringdashboard  as dashboard

class AppFactory:
    def __init__(self):

          self.app = Flask(__name__)
          self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///request.db'
          self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
          db.init_app(self.app)
          dashboard.config.init_from(file='config.cfg')


          from models.request_log import RequestLog

          with self.app.app_context():
              db.create_all()

          fibonacci=FibonacciController()
          power=PowController()
          factorial=FactorialController()
          get_all_requests=GetAllRequestsController()


          self.app.add_url_rule('/pow_function', view_func=power.pow_function, methods=['POST'])
          self.app.add_url_rule('/fibo_function', view_func=fibonacci.fibo_function,methods=['POST'])
          self.app.add_url_rule('/factorial_function',view_func=factorial.factorial_function, methods=['POST'])
          self.app.add_url_rule('/get_all_requests_function',view_func=get_all_requests.get_all_requests_function,methods=['GET'])

          dashboard.bind(self.app)

          @self.app.after_request
          def log_request(response):
              if request.path.startswith("/dashboard"):
                  return response

              logger = RequestLoggingService()

              endpoint = request.path
              method = request.method
              status_code = response.status_code
              request_body = request.get_json(silent=True)
              response_body = None
              if not response.direct_passthrough:
                  response_body = response.get_data(as_text=True)
              timestamp = datetime.utcnow()

              logger.write_log(
                  endpoint=endpoint,
                  method=method,
                  status_code=status_code,
                  request_body=request_body,
                  response_body=response_body,
                  timestamp=timestamp
              )

              return response
    def create_app(self):
          return self.app

app = AppFactory().create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)




