from __future__ import annotations
from random import random


class Mob:
    def __init__(self):
        self.name = "原型"
        self.health = random()*100 + 100
        self.atk = random()*10+10
        self.crit = random()*0.3+0.3

    def attack(self, target: Mob):
        damage = self.atk
        crit = self.crit > random()
        hit = 0.8 > random()

        critMsg = "，爆擊！" if crit else ""
        if(crit):
            damage = damage*1.5

        if(hit):
            target.health = target.health - damage
            return "{} 給予 {} {:.2f} 點傷害 {}".format(self.name, target.name, damage, critMsg)
        else:
            return "{} 沒打到QQ".format(self.name)

    def showStatus(self):
        return "{}：血量{:.2f}，攻擊力{:.2f}，暴擊率{:.2f}%".format(self.name, self.health, self.atk, self.crit*100)

    def showHealth(self):
        return "{} 還有 {:.2f} 滴血".format(self.name, self.health)
