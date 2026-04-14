from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
