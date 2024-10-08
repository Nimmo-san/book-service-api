from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
# MongoDB connection
mongo_uri = os.getenv("MONGO_URI")
# print(mongo_uri)

client = MongoClient(mongo_uri)
db = client['book_db']
books_collection = db['books']

# Data to be inserted (seed data)
seed_data = [
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "published_date": "1951"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_date": "1960"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "published_date": "1949"
    }
]

# Drop existing data if you want a clean slate
if books_collection is not None:
    books_collection.drop()

# Insert the seed data into the collection
books_collection.insert_many(seed_data)

print("Database seeded!")
