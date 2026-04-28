import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Helper function to get DB connection
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Returns dict-like objects
    return conn

# Create tables if they don't exist
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # 1. Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                      (id INTEGER PRIMARY KEY, title TEXT, thumbnail TEXT, rating REAL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS watchlist 
                      (id INTEGER PRIMARY KEY, title TEXT UNIQUE, thumbnail TEXT, rating REAL)''')
    
    # 2. Check if movies table is empty
    cursor.execute("SELECT count(*) FROM movies")
    if cursor.fetchone()[0] == 0:
        # Define your list of movies here (grab this from your old app.py)
        movie_list = [
            ("Inception", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQovCe0H45fWwAtV31ajOdXRPTxSsMQgPIQ3lcZX_mAW0jXV3kH", 4.8),
            ("Interstellar", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oW0XQlu1lo1G_49M-YwGzKR6rUg-CtflZj07HfbT8d2GwKWg", 4.9),
            ("The Dark Knight", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQkUywIUXDjHSQJIaNHYVs08osgBpF5Ot-xmB_omyEZeeRP9Xug", 4.7),
            ("The Matrix", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5DoFtShSmClflZ0RzBj9JBMweU5IUVBCeEbbLeV2XPlCnTKNi", 4.6),
            ("RRR", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRx0wTDoneV8OuMM6hNfD7vfibB_jt6FcCL-u8H2DljlRXgGCoG", 4.6)
        ]
        
        # 3. Bulk Insert
        cursor.executemany("INSERT INTO movies (title, thumbnail, rating) VALUES (?, ?, ?)", movie_list)
        conn.commit()
        print("Database seeded successfully!")
    
    conn.close()

init_db()

@app.route("/movies", methods=["GET"])
def get_movies():
    conn = get_db()
    movies = conn.execute("SELECT * FROM movies").fetchall()
    conn.close()
    return jsonify({"movies": [dict(m) for m in movies]})

@app.route("/watchlist", methods=["POST"])
def add_to_list():
    data = request.json
    try:
        conn = get_db()
        conn.execute("INSERT INTO watchlist (title, thumbnail, rating) VALUES (?, ?, ?)",
                     (data['title'], data['thumbnail'], data['rating']))
        conn.commit()
        conn.close()
        return jsonify({"message": f"{data['title']} added!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Movie already in watchlist"}), 400

@app.route("/watchlist", methods=["GET"])
def get_watchlist():
    conn = get_db()
    watchlist = conn.execute("SELECT * FROM watchlist").fetchall()
    conn.close()
    return jsonify({"watchlist": [dict(w) for w in watchlist]})

if __name__ == "__main__":
    app.run(port=5003, debug=True)