from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from recengine import recommend_movie

app = Flask(__name__)
api = Api(app)


class recommend(Resource):
    def post(self):
        postedData = request.get_json()

        #Get the data
        movieName = postedData["movie_name"]
        number = int(postedData["number"])

        movies = recommend_movie(movieName, number)
        print(movies)

        retJson = {
            "status":200,
            "movies":movies
             }
        return jsonify(retJson)

api.add_resource(recommend, '/recommend')


if __name__=="__main__":
    app.run(host='0.0.0.0')
