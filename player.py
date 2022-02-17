from mob import Mob


class Player(Mob):
    def __init__(self):
        super().__init__()
        self.name = "俗靈"

    def heal(self):
        self.health += 30