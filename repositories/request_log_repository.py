from Microservice_Flask.repositories.database import db


class RequestLogRepository:
    def save(self,log):
        db.session.add(log)
        db.session.commit()