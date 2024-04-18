from tinydb import TinyDB, Query
import os
import json

LOCAL_FOLDER = (os.path.abspath(os.path.join(os.path.dirname(__file__))))
db = TinyDB(os.path.join(LOCAL_FOLDER, 'brain.json'))

class User:
    @classmethod
    def login(cls, form):
        user_data = json.loads(form.decode('utf-8'))
        email = user_data['email']
        password = user_data['password']

        User = Query()

        if db.search(User.email == email) and db.search(User.password == password):
            print("Usuário válido. Pode logar!")

        elif not db.search(User.passoword == password):
            print("Senha incorreta")

        elif not db.search(User.email.exists()):
            print("Usuário não cadastrado. Cadastre-se!")

    @classmethod
    def sign_up(cls, form):
        User = Query()

        if not db.search(User.email.exists()):
            new_user = json.loads(form.decode('utf-8'))

            db.insert(new_user)
            print("Usuário cadastrado!")

        else:
            ("Usuário já existente")
class Article:
    @classmethod
    def load_articles(cls):
        return db.all()

    @classmethod
    def insert(cls, data):
        article = json.loads(data.decode('utf-8'))
        print(article['title'])
        # article = {
        #     "title": data.title,
        #     #"autor": data.author,
        #     "body": data.body,
        #     #"published": data.published
        # }
        db.insert(article)

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass




