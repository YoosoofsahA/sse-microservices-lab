from flask import Flask, render_template, request, jsonify
from books import books

app = Flask(__name__)

def get_data_from_file(title):
    for book in books:
        if book['title'] == title:
            return book
    return None


def get_books_by_genre(genre):
    genre_words = genre.lower().split()
    return [book for book in books if any(word in book['genre'].lower() for word in genre_words)]


@app.route("/")
def default():
    return render_template("index.html")


@app.route("/search-book", methods=["POST"])
def get_data(): 
    title = request.form.get("title")
    data = get_data_from_file(title)
    if data:
            return jsonify(data)
    else:
        return jsonify({"error": "Book not found"})


@app.route("/books", methods=["GET"])
def get_books_genre():
    genre = request.args.get("genre")
    if genre:
        filtered_books = get_books_by_genre(genre)
        return jsonify(filtered_books)
    else:
        return jsonify({"error": "Genre not specified"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)