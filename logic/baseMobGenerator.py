from random import random

# 負責產出隨機的怪物


class baseMobGenberator:
    def create(self, level):
        health = self.__genHealth(level)
        return {
            "discordId": 0,
            "name": "Enemy Lv. {}".format(level),
            "maxHealth": health,
            "health": health,
            "attack": self.__genAttack(level),
            "defence": self.__genDefence(level),
            "luk": self.__genLuk(level),
            "dex": self.__genDex(level),
            "exp": 0,
            "level": level
        }

    def __genHealth(self, level):
        range = random() / 10 + 1
        base = level*50 + 50
        return int(base * range)

    def __genAttack(self, level):
        range = random() / 10 + 1
        base = level*10 + 10
        return int(base * range)

    def __genDefence(self, level):
        range = random() / 10 + 1
        base = level*5 + 5
        return int(base * range)

    def __genLuk(self, level):
        range = random() / 10 + 1
        base = level*2.5 + 2.5
        return int(base * range)

    def __genDex(self, level):
        range = random() / 10 + 1
        base = level*2.5 + 2.5
        return int(base * range)
