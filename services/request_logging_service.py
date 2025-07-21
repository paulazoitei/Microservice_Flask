
from models.request_log import RequestLog
from repositories.database import db

class RequestLoggingService:
    def write_log(self, endpoint, method, status_code, request_body,
                  response_body, timestamp):
        log = RequestLog(
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            request_body=str(request_body),
            response_body=response_body,
            timestamp=timestamp
        )
        db.session.add(log)
        db.session.commit()
