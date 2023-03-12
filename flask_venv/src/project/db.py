from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://binod:binod12@cluster0.r0sdjhp.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db=client.get_database('db_flask')