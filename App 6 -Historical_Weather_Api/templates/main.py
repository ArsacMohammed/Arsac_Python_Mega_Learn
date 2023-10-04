from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Home")
def home():
    return render_template("tutorial.html")


@app.route("/api/<station>/<date>/")
def about(station,date):
    temperature=20
    return {"station":station,"date":date,"temp":temperature}

if(__name__)=="__main__":
    app.run(debug=True)