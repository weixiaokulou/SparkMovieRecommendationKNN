## LikeUberPosition

### Tech in this project
Spark, Neural Network(Deep Leaning) in Spark's mllib

### Installing
What we need: 
Spark, Dataset

Install Spark:
https://medium.freecodecamp.org/installing-scala-and-apache-spark-on-mac-os-837ae57d283f

Download Dataset:
movielens:
https://grouplens.org/datasets/movielens/

### Getting start
Navigate into the project directory:
```
cd SparkMovieRecommendationKNN
```
Put dateset in ./movieData/filename.csv

Start runing Spark scipt:
```
spark-submit SparkDTest.py
```
### Methodology
There are four stages to build the recommend model:
1. Divide the dataset into three parts: training_RDD, validation_RDD, test_RDD.
2. Choose ranks to produce ALS models, then compare the result using validation_RDD.
3. Using the best model produce result for the joined unit of training_RDD and the test for prediction RDD.
4. Add a new user and provide him/her the personal recommendation using the above model.

## Authors

* **Rachel Gao** - *Initial work* - [RachelGao](https://github.com/weixiaokulou)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
