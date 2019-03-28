from pymongo import MongoClient

#1. Connect mongodb
mongo_uri = "mongodb+srv://admin:admin@cluster0-nmvb5.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)

#2. Get / Create database
db_demo = client.test_database #tạo database tên là test_database

#3. Get / Create collection
first_collection = db_demo["my_collection"]

#4. Create document
game_document = {
    "title": "FO4",
    "description": "Fifa online 4",
}

#5. Insert document
first_collection.insert_one(game_document)

#6. READ
#6.1 Read all
all_documents = first_collection.find()
for document in all_documents:
    print(document["title"])

# 6.2 Read one
one_document = first_collection.find_one({"title": "LOL"}) #phải tìm theo dạng dic
print(one_document)