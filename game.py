from enemy import Enemy
from player import Player


class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.enemy = Enemy()
        self.player = Player()

    def showStatus(self):
        return self.player.showStatus() + "\n " + self.enemy.showStatus()

    def showHealth(self):
        return self.player.showHealth() + "\n" + self.enemy.showHealth()

    def heal(self):
        self.player.heal()

    def attack(self):
        return self.player.attack(self.enemy) + "\n" + self.enemy.attack(self.player)

    def check(self):
        if(self.enemy.health < 0):
            return self.enemy.name + "死ㄌ"
        elif(self.player.health < 0):
            return self.player.name + "死ㄌ"
        else:
            return self.showHealth()
