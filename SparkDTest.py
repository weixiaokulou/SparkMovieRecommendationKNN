# from __future__ import print_function

# $example on:init_session$
from pyspark.sql import SparkSession
# $example off:init_session$

from pyspark.sql.functions import *
# $example off:programmatic_schema$

from pyspark.sql import SQLContext


def basic_df_example(sc):
    sqlContext = SQLContext(sc)
    dfmovies = sqlContext.read.format('csv').options(header='true', inferSchema='true').load('./movieData/movies.csv')
    colm_movies = dfmovies.select('movieId','title')

    dfratings = sqlContext.read.format('csv').options(header='true', inferSchema='true').load('./movieData/ratings.csv')
    colm_ratings = dfratings.select('userId','movieId','rating')

    colm_movies.show()
    colm_ratings.show()
    movie_ratings = colm_movies.join(colm_ratings, colm_movies.movieId == colm_ratings.movieId, 'left_outer')
    movie_ratings.show()

    starWarsRatings = movie_ratings.filter("title = 'GoldenEye (1995)'").select(movie_ratings['userId'],movie_ratings['rating'],movie_ratings["title"])
    starWarsRatings.show()
    # starWarsRatings = movie_ratings.filter(movie_ratings["title"]=="Toy Story (1995)").select(movie_ratings['userId'],movie_ratings['rating'],movie_ratings["title"])
    

if __name__ == "__main__":
    # $example on:init_session$
    sc = SparkSession \
        .builder \
        .appName("Finding Similar Movies") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    # $example off:init_session$

    basic_df_example(sc)

    sc.stop()