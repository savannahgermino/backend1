import pymongo
import certifi


con_str = "mongodb+srv://savgermino:J5w*rsC4GS6fs5J@cluster0.pvvo6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Bakery")