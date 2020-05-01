import logging
from logging.handlers import RotatingFileHandler
from flask_restful import Resource
from flask import jsonify, request
from recengine import recommend_movie
from models import SearchMovie

#loging
logging.basicConfig(filename='logInfo.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


class Recommend(Resource):
    def post(self):
        postedData = request.get_json()

        #Get the data
        try:
            movieName = postedData["movie_name"]
            number = int(postedData["number"])
        except Exception as e:
                logging.error('Error! {}'.format(e))
                return "Data not found", 400

        movies = recommend_movie(movieName, number)

        if movies:
            rec_success = True
        else:
            rec_success = False

        #handle Ip
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            ipp_address=request.environ['REMOTE_ADDR']
        else:
            ipp_address=request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
        
        logging.info('Ip address')
      

        #save to db
        try:
            SearchMovie(movie_name=movieName, rec_success=rec_success,
                    rec_movies=movies, ipp_address=ipp_address).save(force_insert=True)
        except Exception as e:
                logging.error('Error! {}'.format(e))
                return "Could not Save", 400
        
        logging.info('saved')
        
        
        retJson = {
            "status":200,
            "movies":movies
             }
    
        return jsonify(retJson)