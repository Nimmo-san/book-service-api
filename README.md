# Book Management API

A simple Flask API that allows users to manage books, including creating, reading, updating, and deleting (CRUD) book records. The API uses MongoDB Atlas for the database and is containerized using Docker.

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
- **MongoClient**: For managing the MongoDB connection.
- **Docker**: Containerization for easy deployment and development.

---

## Setup and Installation

### Prerequisites

1. **Python 3.11.x**: Ensure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).
2. **MongoDB Atlas**: You'll need a MongoDB Atlas account to store the data. [Create an account here](https://www.mongodb.com/cloud/atlas).
3. **Docker**: Ensure Docker is installed if you want to run the project in a container. You can install Docker [here](https://www.docker.com/get-started).

### Steps to Set Up Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/<yourusername>/book-management-api.git
   cd book-management-api
