from flask_restx import Resource, Namespace
from http import HTTPStatus
from app.main.model.user import User

api = Namespace('test', description='Test API', path='/test')


@api.route("/")
class TestAPI(Resource):

    def get(self):
        user = User.query.first()
        return {"test": user}, HTTPStatus.OK
