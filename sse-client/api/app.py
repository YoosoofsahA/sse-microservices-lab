from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# Replace with the FQDN of your first service
FIRST_SERVICE_URL = os.getenv("FIRST_SERVICE_URL", "https://google.com")

@app.route("/")
def default():
    return render_template("index.html")

@app.route('/books', methods=['GET'])
def get_filtered_books():
    genre = request.args.get('genre')

    # Fetch books data from the first service
    url_with_genre = f"{FIRST_SERVICE_URL}?genre={genre}" if genre else FIRST_SERVICE_URL
    response = requests.get(url_with_genre)
    if response.status_code != 200:
        return "Error: Unable to fetch books data", response.status_code

    books = response.json()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)