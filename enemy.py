from random import random
from mob import Mob


class Enemy(Mob):
    def __init__(self):
        super().__init__()
        self.name = "怪物A"
