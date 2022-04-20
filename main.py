from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()


courses = {1: {"name": "Java", "videos" : 10},
           2: {"name": "Kotlin", "videos" : 15},
           3: {"name": "Go", "videos" : 20}}



class Main(Resource):

    def get(self, cources_id):

        if cources_id != 0:
            courses[cources_id]
        else:
            return courses

    def delete(self, cources_id):

        del courses[cources_id]
        return courses

    def post(self, couces_id):

        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("videos", type=int)
        courses[couces_id] = parser.parse_args()
        return courses

    def put(self, cources_id):

        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str)
        parser.add_argument("videos", type=int)
        courses[cources_id] = parser.parse_args()
        return courses



api.add_resource(Main, "/api/courses/<int:cources_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

'''

Бекенд

'''