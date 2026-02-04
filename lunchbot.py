import random
import csv
from flask import Flask, render_template_string

app = Flask(__name__)

# Path to your CSV file
CSV_FILE = "lunch.csv"

def get_random_item():
    with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        items = [row[0] for row in reader if row]  # First column only
    return random.choice(items)

@app.route("/")
def index():
    item = get_random_item()
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LunchBot</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: Arial, sans-serif;
                background: #000000;
            }
            .text {
                font-size: 3rem;
                font-weight: bold;
                color: #FFFFFF;
            .place {
                font-size: 5rem;
                font-weight: bold;
                color: #FFFFFF;
            }
        </style>
    </head>
    <body>
        <p class=text>Ni kan ju för fan gå till {{ item }}</p>
    </body>
    </html>
    """
    return render_template_string(html, item=item)

if __name__ == "__main__":
    app.run(debug=True)