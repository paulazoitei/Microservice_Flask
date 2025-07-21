from repositories.database import db

class RequestLog(db.Model):
    __tablename__ = 'request_logs'

    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(100))
    method = db.Column(db.String(10))
    status_code = db.Column(db.Integer)
    request_body = db.Column(db.Text)
    response_body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
