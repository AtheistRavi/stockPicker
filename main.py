from flask import Flask, render_template
from your_algo_module import get_filtered_stocks

app = Flask(__name__)

@app.route("/")
def home():
    stocks = get_filtered_stocks()  # Fetching dynamically filtered stocks
    return render_template("index.html", stocks=stocks)

if __name__ == "__main__":
    app.run(debug=True)
