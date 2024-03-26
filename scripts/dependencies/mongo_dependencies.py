# dependencies.py
from ..core.handler.mongo_handler import Mongo_Library

class MongoDbDependency:
    def __init__(self):
        self.mongo_handler = Mongo_Library()

    def __call__(self):
        return self.mongo_handler
