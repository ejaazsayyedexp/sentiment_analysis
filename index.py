from flask import Flask, jsonify, request
from preprocessText import preprocess_text
from scraper import get_movie_review
from prediction import predict
from loadModel import load_model
import math


app = Flask("sentiment")


model = load_model()

@app.route('/getMovieReview/<movieName>',methods=['GET'])
def sendReview(movieName):
    total_score = 0
    movie_review = get_movie_review(movieName)
    for x in movie_review:
        movie = preprocess_text(x)
        total_score+=predict(model,movie)
    return str(math.ceil(total_score*10))




if(__name__=='__main__'):
    app.run(port=8000)