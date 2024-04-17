import os
#from database import DB

TIMESTAMP_FORMAT = '@{:%Y%-m%-d% H%:M%}'
LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__)))
URL = "anbubus.pythonanywhere.com"
#PASSWORD = dcd(str.encode(os.environ["ANBUBUS_PASSWORD"])).decode("utf-8")

# db = TinyDB(os.path.join(LOCAL_FOLDER, 'db.json'))


class Article:
    @classmethod
    def get_article(cls, id):
        pass
        #return data[id]
class Facade:
    """modelo que representa interação com o banco de dados"""
    @classmethod
    def create(cls):
        pass
    @classmethod
    def save(cls):
        pass
    @classmethod
    def load(cls, id):
        article = Article.get_article(id)
        return article
    @classmethod
    def delete(cls):
        pass
    @classmethod
    def update(cls):
        pass
    @classmethod
    def init_db_(cls):
        return