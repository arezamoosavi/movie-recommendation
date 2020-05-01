from data import load_data
import operator

movieDict, movies_table = load_data()

def getMovieId(movieName):
    id = movies_table[movies_table['title']==movieName]['movie_id']
    if id.count() > 0:
        return id.values[0]
    else:
        return None

def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))
def cosine_similarity(a,b):
    return 1-(dot(a,b) / ( (dot(a,a) **.5) * (dot(b,b) ** .5) ))


def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = cosine_similarity(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance


def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

def recommend_movie(movieName, number):
    id = getMovieId(movieName)
    if id:
        neighbors = getNeighbors(id, number)
        return [movieDict[neighbor][0] for neighbor in neighbors ]
    else:
        return None