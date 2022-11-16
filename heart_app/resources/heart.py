from flask import Response, request
from database.models import Heart
from flask_restful import Resource
from flask_jwt_extended import jwt_required

class HeartsApi(Resource):
    #1. Create a REST API using FLASK insert a new heart record to a JSON file.
    @jwt_required()
    def post(self):
        body = request.get_json()
        heart_rec = Heart(**body).save()
        id = heart_rec.id
        return {'id': str(id)}, 200


    #2. Create a REST API using FLASK to read a heart information from a JSON file
    def get(self):
        heart_rec = Heart.objects().to_json()
        return Response(heart_rec, mimetype="application/json", status=200)


class HeartApi(Resource):
    #3. Create a REST API using FLASK to read a heart information of a specific heart_id from a JSON file
    def get(self, id):
        heart_rec = Heart.objects.get(heart_id=id).to_json()
        return Response(heart_rec, mimetype="application/json", status=200)

    #4. Create a REST API using FLASK to update a heart record of a specific heart_id 
    @jwt_required()
    def put(self, id):
        body = request.get_json()
        Heart.objects.get(id=id).update(**body)
        return 'Heart was successfully updated', 200
    #5. Create a REST API using FLASK to delete a heart record of a specific heart_id
    @jwt_required()
    def delete(self, id):
        Heart.objects.get(id=id).delete()
        return 'Heart was successfully deleted', 200