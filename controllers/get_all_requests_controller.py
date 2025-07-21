from flask import Flask,jsonify,request
from services.get_all_requests_service import GetAllRequestsService

class GetAllRequestsController:
    def get_all_requests_function(self):

        service=GetAllRequestsService()
        result=service.get_all_requests()

        serialized = []
        for r in result:
            serialized.append({
                "id": r.id,
                "endpoint": r.endpoint,
                "method": r.method,
                "status_code": r.status_code,
                "request_body": r.request_body,
                "response_body": r.response_body,
                "timestamp": r.timestamp.isoformat()
            })

        return jsonify({
            "requests":serialized
        })
