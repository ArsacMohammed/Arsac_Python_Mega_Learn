from flask import Flask, render_template

app = Flask("Weather")


@app.route("/Home")
def home():
    return render_template("tutorial.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact-us/")
def contact_us():
    return render_template("contact_us.html")


@app.route("/store/")
def store():
    return render_template("store.html")

app.run(debug=True)