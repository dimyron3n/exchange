from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # Замість 'YOUR_API_KEY' використовуйте ваш ключ API
    response = requests.get("https://api.exchangerate.host/latest?base=USD")
    data = response.json()
    rates = data.get("conversion_rates", {})
    return render_template("index.html", rates=rates)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
