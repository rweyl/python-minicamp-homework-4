from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/addmovie")
def add_movie():
	return render_template("movie.html")

@app.route("/movie", methods=["POST"])
def new_movie():
	conn = sqlite3.connect("database4.db")
	cur = conn.cursor()

	try:
		title = request.form["title"]
		rating = request.form["rating"]
		runtime = request.form["run_time"]
		print(title,rating,runtime)
		cur.execute("INSERT INTO movies (title,rating,run_time) VALUES (?,?,?)", (title,rating,runtime))
		conn.commit()
		message = "movie added successfully"
	except:
		conn.rollback()
		message = "error inserting movie"
	finally:
		conn.close()
		return message

@app.route("/movies")
def all_movies():
	conn = sqlite3.connect("database4.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM movies")
	movie_list = cur.fetchall()
	conn.close()
	return jsonify(movie_list)

@app.route("/search", methods=["GET"])
def search():
	conn = sqlite3.connect("database4.db")
	cur = conn.cursor()

	title = request.args["title"]
	cur.execute("SELECT * FROM movies WHERE title=?", [title]) 
	results = cur.fetchone()
	conn.close()
	return jsonify(results)
