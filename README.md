# MovieRecSystem

This project is asynchronous web service that uses a KNN algorithm to recommend movies based on a favorite posted movie_name by user. The whole web framework is built on flask, gunicorn, nginx and mongodb and machine learning tasks is asynched with celery, rabbitmq and redis.

## Installation

for creating the project:
```bash
docker-compose up --build -d
```
to stop it
```bash
docker-compose down -v
```
to bash in a container like database:
```bash
docker exec -it recsys_db_1 bash
```

## Usage
to get recommended movie:
number means how many movie would you like to get.

```bash
curl -H "Content-Type: application/json" -X POST -d 
'{"movie_name":"Once Upon a Time in America (1984)","number":6}' http://0.0.0.0:8000/recommend
```
to see admin panel:
```bash
http://0.0.0.0:8000/admin
```
## Result

![alt text](https://github.com/arezamoosavi/movie-recommendation/blob/master/resultpanel.jpeg?raw=true)