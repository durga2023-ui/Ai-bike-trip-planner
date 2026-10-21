
from flask import Flask, render_template, request
from urllib.parse import quote

app = Flask(__name__)

# Sample tourist places database
places = [
    {
        "name": "Marina Beach",
        "city": "Chennai",
        "category": "Beach",
        "distance": 5,
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },
    {
        "name": "Meenakshi Amman Temple",
        "city": "Madurai",
        "category": "Temple",
        "distance": 3,
        "image": "https://images.unsplash.com/photo-1600100397608-f010e3e5c7c5"
    },
    {
        "name": "Ooty Lake",
        "city": "Ooty",
        "category": "Nature",
        "distance": 2,
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e"
    },
    {
        "name": "Adiyogi Shiva Statue",
        "city": "Coimbatore",
        "category": "Spiritual",
        "distance": 30,
        "image": "https://images.unsplash.com/photo-1518837695005-2083093ee35b"
    },
    {
        "name": "Thirumalai Nayakkar Mahal",
        "city": "Madurai",
        "category": "Historical",
        "distance": 2,
        "image": "https://images.unsplash.com/photo-1595658658481-d53d3f999875"
    },
    {
        "name": "Doddabetta Peak",
        "city": "Ooty",
        "category": "Mountain",
        "distance": 10,
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b"
    }
]


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    location = ""
    max_distance = 100
    searched = False

    if request.method == "POST":
        location = request.form.get("location", "").strip()
        max_distance = int(request.form.get("distance", 100))
        searched = True

        for place in places:
            if (
                location.lower() in place["city"].lower()
                and place["distance"] <= max_distance
            ):
                item = place.copy()
                item["map_url"] = (
                    "https://www.google.com/maps/dir/"
                    + quote(location)
                    + "/"
                    + quote(item["name"] + ", " + item["city"])
                )
                results.append(item)

    return render_template(
        "index.html",
        places=results,
        location=location,
        distance=max_distance,
        searched=searched
    )


if __name__ == "__main__":
    app.run(debug=True)
