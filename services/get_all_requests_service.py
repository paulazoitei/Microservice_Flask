from repositories.database import db
from models.request_log import RequestLog

class GetAllRequestsService:
    def get_all_requests(self):
        requests=RequestLog.query.all()
        return requests
