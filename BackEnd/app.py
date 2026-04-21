from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database
all_movies = [
    {"id": 1, "title": "Inception", "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQovCe0H45fWwAtV31ajOdXRPTxSsMQgPIQ3lcZX_mAW0jXV3kH", "rating": 4.8},
    {"id": 2, "title": "Interstellar", "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9oW0XQlu1lo1G_49M-YwGzKR6rUg-CtflZj07HfbT8d2GwKWg", "rating": 4.9},
    {"id": 3, "title": "The Dark Knight", "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQkUywIUXDjHSQJIaNHYVs08osgBpF5Ot-xmB_omyEZeeRP9Xug", "rating": 4.7},
    {"id": 4, "title": "The Matrix", "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5DoFtShSmClflZ0RzBj9JBMweU5IUVBCeEbbLeV2XPlCnTKNi", "rating": 4.6},
    {"id": 5, "title": "The Lord of the Rings: The Fellowship of the Ring", "thumbnail": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSYHuKZScdd6RHhzh-IDKga3wfTTd9cPEe1Y2JUI5gjvaxgJc3O", "rating": 4.8},
    {"id": 6, "title": "Dhurandhar", "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAHn3l83WxU4xzIgbGq0WqTG4GJbOW7flby7Y8PEh2ueVAbYO_", "rating": 4.7 },
    {"id": 7, "title": "RRR", "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRx0wTDoneV8OuMM6hNfD7vfibB_jt6FcCL-u8H2DljlRXgGCoG", "rating": 4.6 },
    {"id": 8, "title": "Jawan", "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA8fxJgOk6Q4UGjmsa1q3CQ1Q05Lt0Dn1leAl6_KexCEjqJAe6", "rating": 4.5 },
    {"id": 9, "title": "Mirzapur", "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQyP8kYiwrOhEHB8b_r1hDBnw7Boeeget8D8s0qq3Zm8Jx8UZf7", "rating": 4.8 },
    {"id": 10, "title": "Sacred Games", "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTyI-N4Sy-tDcLM93Z0049o6nuIi_afh8T2K5MyVRJ5FxY6Aj4a", "rating": 4.7 },
]
my_watchlist = []

# READ: Get all movies (GET)
@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify({"movies": all_movies})


# CREATE: Add to watchlist (POST)
@app.route("/watchlist", methods=["POST"])
def add_to_list():
    data = request.json
    my_watchlist.append(data)
    print(f"Watchlist updated: {my_watchlist}")
    return jsonify({"message": f"{data['title']} Added to watchlist!"}), 201

# READ: Get all watchlist items (GET)
@app.route("/watchlist", methods=["GET"])
def get_watchlist():
    return jsonify({"watchlist": my_watchlist})

# Server Port(5002)
if __name__ == "__main__":
    app.run(port=5002, debug=True)#