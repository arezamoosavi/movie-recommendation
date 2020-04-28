from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from data import load_data

app = Flask(__name__)
api = Api(app)
moviesDict, movies_table = load_data()


def MovieId(movieName):
    id = movies_table[movies_table['title']==movieName]['movie_id']
    if id.count() > 0:
        return id.values[0]
    else:
        return None


class recommend(Resource):
    def post(self):
        postedData = request.get_json()

        #Get the data
        movieName = postedData["movie_name"]
        number = postedData["number"]

        movieId = MovieId(movieName)
        print(movieId)

        retJson = {
            "status":200,
            "movieId": int(movieId),
            "movieName":movieName
             }
        return jsonify(retJson)

api.add_resource(recommend, '/recommend')


if __name__=="__main__":
    app.run(host='0.0.0.0')
