import pymongo
from ..db.Mongo_db.m_db import mongo_db

connection_string = "mongodb+srv://joshnaj123:joshna%40123@librarymanagementsystem.2dn2jpw.mongodb.net/Library_management_system"  
my_mongo_db = mongo_db(connection_string)
