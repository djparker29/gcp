import yfinance as yf
import pandas as pd

from flask import Flask, render_template, request 

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/", methods=["POST"])
def my_form_post():
  # Configuration variables

  start = '2020-12-31'
  end = '2021-01-02'

  ticker = request.form["ticker"]
  # start = request.form["start_date"]
  # end = request.form["end_date"]

  data = yf.Ticker(ticker)
  df = data.history(start=start, end=end)
  price = round(df.iloc[0]["Close"], 2)

  return render_template("index.html", ticker=ticker, price=price)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))