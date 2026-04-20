from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database
all_movies = [
    {"id": 1, "title": "Inception", "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQovCe0H45fWwAtV31ajOdXRPTxSsMQgPIQ3lcZX_mAW0jXV3kH", "rating": 4.8},
    {"id": 2, "title": "Interstellar", "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oW0XQlu1lo1G_49M-YwGzKR6rUg-CtflZj07HfbT8d2GwKWg", "rating": 4.9}
]
my_watchlist = []

# READ: Get all movies (GET)
# NOTE: The path is now /products to match your frontend fetch()
@app.route("/products", methods=["GET"])
def get_movies():
    return jsonify({"products": all_movies})

# CREATE: Add to watchlist (POST)
@app.route("/watchlist", methods=["POST"])
def add_to_list():
    data = request.json
    my_watchlist.append(data)
    print(f"Watchlist updated: {my_watchlist}")
    return jsonify({"message": f"{data['title']} added to watchlist!"}), 201

if __name__ == "__main__":
    app.run(port=5001, debug=True)