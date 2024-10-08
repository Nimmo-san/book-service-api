from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flasgger import Swagger
# from dotenv import load_env
import os


app = Flask(__name__)
swagger = Swagger(app)

#Mongo db config 
app.config['MONGO_URI'] = os.getenv('MONGO_URI', "mongodb://localhost:27017/book_db")
mongo = PyMongo(app)

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "OK"}), 200

# Create a book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    published_date = data.get('published_date')

    if not title or not author:
        return jsonify({"error": "Title and Author are required"}), 400

    book_id = mongo.db.books.insert_one({
        "title": title,
        "author": author,
        "published_date": published_date
    }).inserted_id

    return jsonify({"message": "Book created", "book_id": str(book_id)}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = mongo.db.books.find()
    return dumps(books), 200

# Get a single book
@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return dumps(book), 200

# Update a book
@app.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    mongo.db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": data}
    )
    return jsonify({"message": "Book updated"}), 200

# Delete a book
@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    result = mongo.db.books.delete_one({"_id": ObjectId(book_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"message": "Book deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)