from __future__ import annotations
from random import random

from equips import Equips


class Mob:
    def __init__(self):
        self.name = "ProtoType"
        self.health = 100
        self.mana = 100
        self.attack = 20
        self.defence = 15
        self.dex = 5
        self.luk = 5
        self.exp = 0
        self.level = 1
        self.equips = Equips()
        self.items = []
        self.skills = []