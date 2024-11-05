from pymongo import MongoClient
client = MongoClient()

client = MongoClient("mongodb://localhost:27017")

db = client.test_database

print(db)

collection = db.test_collection

new_document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(new_document)

query = collection.find_one()
print(query)