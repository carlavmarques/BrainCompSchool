import os
import aiohttp
import asyncio
from tinydb import TinyDB

TIMESTAMP_FORMAT = '@{:%Y%-m%-d% H%:M%}'
LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__)))
URL = "http://anbubus.pythonanywhere.com"
# USER = "ANBUBUS"
# PASSWORD = "1234"

db = TinyDB(os.path.join(LOCAL_FOLDER, "brain.json"))
data=[]
"""
    Teste de chamada assincrona:
    Como os dados serão guardados em uma API no PyAnywhere essa foi uma 
    tentativa de iniciar uma estrutura que trate de buscar vários conteudos
    de forma asicrona.
    O teste aqui é com um dado só, porém espera-se que venha bastante ehehe
"""

def get_content(session):

    content = session.get(URL, ssl=False)
    return content
async def fech_data():
    conn = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=conn, trust_env=True) as session:
        response = await get_content(session)
        data.append(await response.json())
        print(data[0])
        db.insert(data[0])

asyncio.run(fech_data())