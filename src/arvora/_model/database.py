from tinydb import TinyDB, Query
from tinydb.operations import delete
import os
import json

LOCAL_FOLDER = (os.path.abspath(os.path.join(os.path.dirname(__file__))))
db = TinyDB(os.path.join(LOCAL_FOLDER, 'brain.json'))

# class Database:
#     @classmethod
#     def get(cls):
#         return db.all()
#     @classmethod
#     def insert(cls, content):
#         for data in content:
#             article = {
#                 "title": data.title,
#                 "autor": data.author,
#                 "body": data.body,
#                 "published": data.published
#             }
#             db.insert(article)

#     @classmethod
#     def update(cls):
#         pass

#     @classmethod
#     def delete(cls):
#         pass

class LoginAndSignUp:

    @classmethod
    def login(cls, form):
        email = form.email
        password = form.password
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
            new_user = {
                "email": form.email,
                "password": form.password,
                "phone": form.phone,
                "name": form.name
            }

            db.insert(new_user)
            print("Usuário cadastrado!")

        else:
            ("Usuário já existente")
