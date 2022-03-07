from random import random
from pymongo import MongoClient


class playerManager:
    """ 負責處理玩家有關的所有資料 """

    def __init__(self):
        self.db = MongoClient("mongodb://localhost:27017/")["database"]
        self.players = self.db["player"]

    def create(self, discordId, name):
        data = {
            "discordId": discordId,
            "name": name,
            "maxHealth": 100,
            "health": 100,
            "attack": 20,
            "defence": 10,
            "luk": 5,
            "dex": 5,
            "exp": 0,
            "level": 1
        }
        return self.players.insert_one(data).inserted_id

    def find(self, discordId):
        return self.players.find_one({"discordId": discordId})
