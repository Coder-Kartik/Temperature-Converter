from flask import Flask, request, render_template
from converter import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        temp = float(request.form["temp"])
        choice = request.form["choice"]
        conversions = {
            "C-F": celsius_to_fahrenheit,
            "F-C": fahrenheit_to_celsius,
            "C-K": celsius_to_kelvin,
            "K-C": kelvin_to_celsius,
            "F-K": fahrenheit_to_kelvin,
            "K-F": kelvin_to_fahrenheit
        }
        if choice in conversions:
            result = conversions[choice](temp)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
