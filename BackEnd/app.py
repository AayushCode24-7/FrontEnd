from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database
all_movies = [
    {"id": 1, "title": "Inception", "thumbnail": "https://bit.ly/3v8X6zX", "rating": 4.8},
    {"id": 2, "title": "Interstellar", "thumbnail": "https://bit.ly/3v7Y7aY", "rating": 4.9}
]
my_watchlist = []

# READ: Get all movies (GET)
@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify({"products": all_movies})

# CREATE: Add to watchlist (POST - FS 20)
@app.route("/watchlist", methods=["POST"])
def add_to_list():
    data = request.json
    my_watchlist.append(data)
    return jsonify({"message": "Movie Added!", "current_list": my_watchlist}), 201

@app.route("/")
def home():
    return "Server is running! Use /movies to see the data."

if __name__ == "__main__":
    app.run(port=5001, debug=True)
    
# In-memory storage for now (Easy to explain in VIVA)
watchlist = []

@app.route('/api/movies', methods=['GET'])
def get_movies():
    # This will be where you later connect to a database
    movies = [
        {"id": 1, "title": "Inception"},
        {"id": 2, "title": "Interstellar"}
    ]
    return jsonify(movies)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

