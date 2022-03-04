from flask_restx import Resource, Namespace
from http import HTTPStatus

api = Namespace('test', description='Test API', path='/test')

@api.route("/")
class TestAPI(Resource):

    def get(self):
        return {"test": "success"}, HTTPStatus.OK

