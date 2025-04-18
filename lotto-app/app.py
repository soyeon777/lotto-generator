from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    lotto_numbers = []
    if request.method == "POST":
        lotto_numbers = sorted(random.sample(range(1, 46), 6))
    return render_template("index.html", numbers=lotto_numbers)

if __name__ == '__main__':
    app.run(debug=True)