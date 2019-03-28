from pymongo import MongoClient

mongo_uri =  "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db = client.c4e
post = db["posts"]

my_document = {
    'title': "lớp học c4e27",
    'author': "HJK :))",
    'content': "học cùng mấy thằng bạn toàn ngáo chó =))",
}

post.insert_one(my_document)
