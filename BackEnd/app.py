import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                      (id INTEGER PRIMARY KEY, title TEXT, thumbnail TEXT, rating REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS watchlist 
                      (id INTEGER PRIMARY KEY, title TEXT UNIQUE, thumbnail TEXT, rating REAL)''')
    
    cursor.execute("SELECT count(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        movie_list = [
            ("Inception", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQovCe0H45fWwAtV31ajOdXRPTxSsMQgPIQ3lcZX_mAW0jXV3kH", 4.8),
            ("Interstellar", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oW0XQlu1lo1G_49M-YwGzKR6rUg-CtflZj07HfbT8d2GwKWg", 4.9),
            ("The Dark Knight", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQkUywIUXDjHSQJIaNHYVs08osgBpF5Ot-xmB_omyEZeeRP9Xug", 4.7),
            ("The Matrix", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5DoFtShSmClflZ0RzBj9JBMweU5IUVBCeEbbLeV2XPlCnTKNi", 4.6),
            ("RRR", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRx0wTDoneV8OuMM6hNfD7vfibB_jt6FcCL-u8H2DljlRXgGCoG", 4.6),
            ("The Conjuring: The Last Rites", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTOpsfBLMRdOZg4ccC2IMNPjc87uLcNiBKZZOGWYRmdzQeSKrkw", 4.2),
        ]
        cursor.executemany("INSERT INTO movies (title, thumbnail, rating) VALUES (?, ?, ?)", movie_list)
        conn.commit()
    conn.close()

init_db()

@app.route("/movies", methods=["GET"])
def get_movies():
    conn = get_db()
    movies = conn.execute("SELECT * FROM movies").fetchall()
    conn.close()
    return jsonify({"movies": [dict(m) for m in movies]})

@app.route("/watchlist", methods=["GET"])
def get_watchlist():
    conn = get_db()
    watchlist = conn.execute("SELECT * FROM watchlist").fetchall()
    conn.close()
    return jsonify({"watchlist": [dict(w) for w in watchlist]})

@app.route("/watchlist", methods=["POST"])
def add_to_list():
    data = request.json
    conn = get_db()
    try:
        conn.execute("INSERT INTO watchlist (title, thumbnail, rating) VALUES (?, ?, ?)",
                     (data['title'], data['thumbnail'], data['rating']))
        conn.commit()
        return jsonify({"message": f"{data['title']} added!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Movie already in watchlist"}), 400
    finally:
        conn.close()

@app.route("/watchlist/<string:title>", methods=["DELETE"])
def remove_from_watchlist(title):
    conn = get_db()
    try:
        conn.execute("DELETE FROM watchlist WHERE title = ?", (title,))
        conn.commit()
        return jsonify({"message": f"{title} removed!"}), 200
    finally:
        conn.close()

@app.route("/search", methods=["GET"])
def search_movies():
    query = request.args.get("q", "").strip()
    conn = get_db()
    movies = conn.execute("SELECT * FROM movies WHERE title LIKE ?", (f"%{query}%",)).fetchall()
    conn.close()
    return jsonify({"movies": [dict(m) for m in movies]})

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=5003, debug=True)