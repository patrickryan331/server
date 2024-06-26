import pymongo
import certifi     ## security encryption


con_str="mongodb+srv://test2:test@cluster0.hffigz5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_str,tlsCAFile=certifi.where())
db = client.get_database("project1")

