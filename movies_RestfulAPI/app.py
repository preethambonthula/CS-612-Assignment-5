import json
from flask import Flask, jsonify, render_template, request, Response


app = Flask(__name__)


with open('marvel.JSON') as json_data:
    d = json.load(json_data)
    list_of_movies = []
    for data in d['DCUMovies']:
    	list_of_movies.append(data)

@app.route('/', methods =['GET'])
def home():
    print("movies", list_of_movies)
    return render_template("index.html")

@app.route('/movies/', methods =['GET'])
def allMovies():
	typefilter = request.args.get('type')
	if (typefilter == 'json'):
		return jsonify(d)
	return render_template("index.html", list_data=list_of_movies)

@app.route('/movies/<string:year>', methods = ['GET'])
def getMoviesByYear(year):
	typefilter = request.args.get('type')
	myList = [movie for movie in list_of_movies if movie['Year'] == year]
	print("mylist", myList)
	if(typefilter == 'json'):
		return jsonify(myList)
	return render_template("index.html", list_data=myList)


if __name__ == '__main__':
	 app.run(host='0.0.0.0', port=5000)