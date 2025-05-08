import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
# db = client.album_database
db = client.Cluster1
album_collection = db.albums

def get_random_album():
    pipeline = [{"$sample": {"size": 1}}]
    result = list(album_collection.aggregate(pipeline))
    if result:
        return result[0]
    return None

def initialize_db():
    count = album_collection.count_documents({})
    return count > 0

