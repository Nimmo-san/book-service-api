from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from flasgger import Swagger
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)


load_dotenv()

app = Flask(__name__)
swagger = Swagger(app)
app.logger.info("Starting the Flask app")

# Mongo db config 
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo_client = MongoClient(os.getenv('MONGO_URI'))
# Initialize PyMongo
db = mongo_client["book_db"]


# Health Check Endpoint
@app.route("/", methods=["GET"])
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200


# Create a book
@app.route("/books", methods=["POST"])
def create_book():
    try:
        app.logger.info("\nCreating a book...\n")
        data = request.json
        title = data.get("title")
        author = data.get("author")
        published_date = data.get("published_date")

        if not title or not author:
            app.logger.warning("\nCreating a book requires title and author\n")
            return jsonify({"error": "Title and Author are required"}), 400

        book_id = db.books.insert_one(
            {"title": title, "author": author, "published_date": published_date}
        ).inserted_id
        app.logger.info(f"\nCreated a book with author/title {author}/{title}\n")
        return jsonify({"message": "Book created", "book_id": str(book_id)}), 201
    except Exception as e:
        app.logger.error(f"\nUnexpected error occurred: {e}\n")
        print(f"Error creating a book: {e}")
        return jsonify({"error": "An error occurred while creating books"}), 500

# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    try:
        app.logger.info("\nFetching collection names...\n")
        print("Connected to MongoDB:", db.list_collection_names())
        
        books = db.books.find()
        books_list = list(books)
        
        app.logger.info("\nReturning the list of books\n")
        return dumps(books_list), 200
    except Exception as e:
        app.logger.error(f"\nUnexpected error occurred: {e}\n")
        print(f"Error fetching books: {e}")
        return jsonify({"error": "An error occurred while fetching books"}), 500



# Get a single book
@app.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    try:
        app.logger.info(f"\nFetching a book with id {book_id}\n")
        book = db.books.find_one({"_id": ObjectId(book_id)})
        if not book:
            app.logger.warning(f"\nBook with id {book_id} does not exist\n")
            return jsonify({"error": "Book not found"}), 404
        return dumps(book), 200
    except Exception as e:
        app.logger.error(f"\nUnexpected error occurred: {e}\n")
        print(f"Error occurred while getting a book with id {book_id}: {e}")
        return jsonify({"error": "An error occurred while updating a book"}), 500

# Update a book
@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        app.logger.info(f"\nUpdating a book with id {book_id}\n")
        data = request.json
        db.books.update_one({"_id": ObjectId(book_id)}, {"$set": data})
        return jsonify({"message": "Book updated"}), 200

    except Exception as e:
        app.logger.error(f"\nUnexpected error occurred: {e}\n")
        print(f"Error occurred while updating a book: {e}")
        return jsonify({"error": "An error occurred while updating a book"}), 500

# Delete a book
@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        app.logger.info(f"\nIn the process of deleting book with id {book_id}\n")
        result = db.books.delete_one({"_id": ObjectId(book_id)})
        if result.deleted_count == 0:
            app.logger.warning(f"\nBook with id {book_id} does not exist\n")
            return jsonify({"error": "Book not found"}), 404
        
        app.logger.warning(f"\nBook with id {book_id} successfully deleted\n")
        return jsonify({"message": "Book deleted"}), 200
    except Exception as e:
        app.logger.error(f"\nUnexpected error occurred: {e}\n")
        print(f"Error deleting book: {e}")
        return jsonify({"error": "An error occurred while fetching books"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
