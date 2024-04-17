from tinydb import TinyDB
import os
import json

LOCAL_FOLDER = (os.path.abspath(os.path.join(os.path.dirname(__file__))))
db = TinyDB(os.path.join(LOCAL_FOLDER, 'brain.json'))

class Database:
    @classmethod
    def get(cls):
        return db.all()

    @classmethod
    def insert(cls, content):
        for data in content:
            article = {
                "title": data.title,
                "autor": data.author,
                "body": data.body,
                "published": data.published
            }
            db.insert(article)

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass




