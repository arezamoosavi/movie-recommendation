# MovieRecSystem

This project uses a KNN algorithm to recommend movies based on a favorite posted movie_name by user. The whole web framework is built on flask, gunicorn, nginx and mongodb with docker images.

## Installation


```bash
docker-compose up --build
```

## Usage

```bash
curl -H "Content-Type: application/json" -X POST -d 
'{"movie_name":"Once Upon a Time in America (1984)","number":6}' http://0.0.0.0:8000/recommend
```