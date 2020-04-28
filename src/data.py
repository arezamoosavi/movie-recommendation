import pandas as pd
import numpy as np

def getmovieNormalizedNumRatings():
    r_cols = ['user_id', 'movie_id', 'rating']
    ratings = pd.read_csv('ml-100k/u.data', sep='\t',
                        names=r_cols, usecols=range(3), engine='python')
    
    
    movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

    movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
    movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
    return movieNormalizedNumRatings, movieProperties

def getMoviesTable():
    m_cols = ['movie_id', 'title']
    movies_table = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols,
                                 usecols=range(2),engine='python')
    return movies_table

def getMoviesDict():
    movieDict = {}
    movieNormalizedNumRatings, movieProperties = getmovieNormalizedNumRatings()
    with open(r'ml-100k/u.item', encoding = "ISO-8859-1") as f:
        temp = ''
        for line in f:
            fields = line.rstrip('\n').split('|')
            movieID = int(fields[0])
            name = fields[1]
            genres = fields[5:25]
            genres = list(map(int, genres))
            movieDict[movieID] = (name, genres, movieNormalizedNumRatings.loc[movieID].get('size'),
                                     movieProperties.loc[movieID].rating.get('mean'))
    
    return movieDict

def load_data():
    movies_table = getMoviesTable()
    moviesDict = getMoviesDict()

    return moviesDict, movies_table