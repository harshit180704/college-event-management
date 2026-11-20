
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
print("College Event Management - Jenkins CI/CD Deployment v2")

events = [
    {"id": 1, "name": "Tech Fest 2026", "date": "2026-12-10",
     "venue": "College Auditorium", "category": "Technology"},
    {"id": 2, "name": "Cultural Night", "date": "2026-12-15",
     "venue": "Main Ground", "category": "Cultural"},
    {"id": 3, "name": "Sports Meet", "date": "2026-12-20",
     "venue": "Sports Complex", "category": "Sports"}
]

registrations = []
next_id = 4


@app.route("/")
def home():
    return render_template(
        "index.html",
        events=events,
        registrations=registrations
    )


@app.route("/add", methods=["POST"])
def add_event():
    global next_id

    name = request.form.get("name", "").strip()
    date = request.form.get("date", "")
    venue = request.form.get("venue", "").strip()
    category = request.form.get("category", "")

    if name and date and venue and category:
        events.append({
            "id": next_id,
            "name": name,
            "date": date,
            "venue": venue,
            "category": category
        })
        next_id += 1

    return redirect(url_for("home"))


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("student", "").strip()
    event_id = request.form.get("event_id", "")

    if name and event_id:
        registrations.append({
            "student": name,
            "event_id": event_id
        })

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
