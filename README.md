# Book Management API

A simple Flask API that allows users to manage books, including creating, reading, updating, and deleting (CRUD) book records. The API uses MongoDB Atlas for the database and is containerized using Docker.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup--installation)
- [Running the Project with Docker](#running-the-project-with-docker)
- [API Endpoints](#api-endpoints)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)

## Features

- Create a new book
- Get a list of all books
- Retrieve details of a specific book by ID
- Update an existing book
- Delete a book

## Technologies Used

- **Flask**: Python-based micro web framework for building the API.
- **MongoDB Atlas**: Cloud-based NoSQL database for storing book records.
- **PyMongo**: Python library for interacting with MongoDB.
- **MongoClient**: For managing the MongoDB connection if necessary
- **Docker**: Containerization for easy deployment and development.

---

## Setup & Installation

### Prerequisites

1. **Python 3.11.x**: Ensure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).
2. **MongoDB Atlas**: You'll need a MongoDB Atlas account to store the data. [Create an account here](https://www.mongodb.com/cloud/atlas).
3. **Docker**: Ensure Docker is installed if you want to run the project in a container. You can install Docker [here](https://www.docker.com/get-started).

### Steps to Set Up Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Nimmo-san/book-service-api.git
   cd book-service-api

2. **Activate the virtual environment**

   ``` python 
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. **Install the dependencies**

   ``` python
   pip install -r requirements.txt

4. **Set up your environment variables**

   Create a .env file in the project root with the following content:
   ``` bash
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?retryWrites=true&w=majority

5. **Run the Flask app**
   
   ``` python
   python app.py

6. **Access the API**

   The API will be accessible at http://localhost:5000.

## Running the Project with Docker

   If you prefer to run the project inside Docker containers:

   Ensure Docker is running on your machine.
   Build and run the Docker container:
   ``` bash
   docker-compose up --build
   ```
   The app should now be accessible at http://localhost:5000.

## API Endpoints

1. Create a New Book URL: ```/books```
   
   Method: POST
   
   Request Body:
   ```json
   {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_date": "1925"
   }
   ```
   Response:
   ``` json
   {
      "message": "Book created",
      "book_id": "1a2b3c4d5e6f"
   }
2. Get All Books URL: ```/books```

   Method: GET

   Response:
   ```json
   [
      {
         "_id": "1a2b3c4d5e6f",
         "title": "The Great Gatsby",
         "author": "F. Scott Fitzgerald",
         "published_date": "1925"
      }
   ]
   ```
3. Get a Book by ID URL: ```/books/{book_id}```

   Method: GET

   Response:
   ```json
   {
      "_id": "1a2b3c4d5e6f",
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_date": "1925"
   }

4. Update a Book URL: ```/books/{book_id}```

   Method: PUT

   Request Body:
   ```json
   {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "published_date": "1925"
   }
   ```
   Response:
   ```json
   {
      "message": "Book updated"
   }

5. Delete a Book URL: ```/books/{book_id}```

   Method: DELETE
   
   Response:
   ```json
   {
      "message": "Book deleted"
   }
   ```
## Testing the API

   You can use **Postman** or **curl** to test the API endpoints:

## Contributing

   Contributions are welcome! If you'd like to contribute:

      1. Fork the repository.

      2. Create a new branch (git checkout -b feature/new-feature).

      3. Commit your changes (git commit -m 'Add new feature).

      4. Push to the branch (git push origin feature/new-feature).

      5. Open a Pull Request.
