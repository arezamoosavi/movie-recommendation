from flask_restful import Resource
from flask import jsonify, request
from recengine import recommend_movie
from models import SearchMovie

class Recommend(Resource):
    def post(self):
        postedData = request.get_json()

        #Get the data
        movieName = postedData["movie_name"]
        number = int(postedData["number"])

        movies = recommend_movie(movieName, number)
        print(movies)

        if movies:
            rec_success = True
        else:
            rec_success = False

        #handle Ip
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ipp_address=request.environ['REMOTE_ADDR']
        else:
            ipp_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy

        print(ipp_address)
        
        #save to db
        SearchMovie(movie_name=movieName, rec_success=rec_success,
                    rec_movies=movies, ipp_address=ipp_address).save(force_insert=True)

        retJson = {
            "status":200,
            "movies":movies
             }
    
        return jsonify(retJson)