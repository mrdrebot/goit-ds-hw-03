import json
from pymongo import MongoClient

def main():
    # Connecting to MongoDB
    client = MongoClient("mongodb+srv://cytric:Q1w2e3r$@cluster0.kx21d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # MongoDB server address
    db = client["module3_task2"]  # Database name
    authors_collection = db["authors"]  # Collection name
    qoutes_collection = db["qoutes"]  # Collection name

    # Uploading a JSON file
    with open("./files/authors.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # Loading JSON data in Python

    # Data type check (array or object)
    if isinstance(data, list):
        authors_collection.insert_many(data)  # Loading an array of JSON objects
    else:
        authors_collection.insert_one(data)  # Loading one object

    # Uploading a JSON file
    with open("./files/qoutes.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # Loading JSON data in Python

    # Data type check (array or object)
    if isinstance(data, list):
        qoutes_collection.insert_many(data)  # Loading an array of JSON objects
    else:
        qoutes_collection.insert_one(data)  # Loading one object

    print("Data successfully loaded into MongoDB!")

if __name__ == "__main__":
    main()