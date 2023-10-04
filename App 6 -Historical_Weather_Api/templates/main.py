from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/Home")
def home():
    return render_template("tutorial.html")


@app.route("/api/<station>/<date>/")
def about(station, date):
    filename = r"C:\Users\mm\Arsac_Python_Mega_learn\Python\App 6 -Historical_Weather_Api\data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, sep=",", skiprows=20, parse_dates=["    DATE"])

    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temp": temperature}


if __name__ == "__main__":
    app.run(debug=True)
