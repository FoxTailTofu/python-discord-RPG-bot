import math
import random


class battleManager:
    """ 負責處理和對戰有關的邏輯 """

    def __init__(self, players: list, enemy: list):
        for actor in players:
            actor["team"] = "player"
        for actor in enemy:
            actor["team"] = "enemy"

        self.players = players
        self.enemy = enemy
        self.queue = []
        self.log = []
        self.isBattleEnd = False
        self.winner = None
        self.round = 1

    def main(self):
        """ 戰鬥邏輯 """
        self.genQueue()
        while(not self.isBattleEnd):
            actor = self.getNextActor()
            self.log.append(
                "\n==> R{}, {} 的回合 <==".format(self.round, actor['name']))
            self.round += 1
            self.useItem(actor)
            # self.useSkill(actor)
            self.doAttack(actor)
            # self.rollEvent(actor)
            self.checkBattleEnd()
        self.log.append("戰鬥結束，{}方勝利".format(self.winner))

    def genQueue(self):
        """ 產生初始戰鬥順序 """
        allActor = self.players.copy()
        allActor.extend(self.enemy)
        random.shuffle(allActor)
        self.queue = allActor

    def getNextActor(self):
        """ 取得下一個行動者 """
        actor = self.queue.pop(0)
        self.queue.append(actor)
        return actor

    def useItem(self, actor):
        """ 使用道具 """
        if(actor['discordId'] == 0):  # 玩家才用道具
            return
        if(random.random() < 0.5):
            return

        regen = math.floor(actor['maxHealth'] * 0.33)
        actor['health'] += regen
        if(actor['health'] > actor['maxHealth']):
            actor['health'] = actor['maxHealth']
        self.log.append("{} 嗑藥，回復了 {} HP".format(actor['name'], str(regen)))
        return

    def useSkill(self, actor):
        """ 使用技能 """
        pass

    def doAttack(self, actor):
        """ 攻擊動作 """
        # 取得攻擊對象
        if(actor["team"] == "player"):
            target = random.choice(self.enemy)
        else:
            target = random.choice(self.players)
        # 傷害計算
        range = random.random()*0.2 + 0.9
        damage = actor["attack"] - target["defence"]
        damage = int(max(damage, actor["attack"] * 0.1) * range)

        # 實際扣血
        target["health"] -= damage
        if(target["health"] < 0):
            target["health"] = 0
        self.log.append("{} 攻擊 {}，造成 {} 點傷害， {} 剩下 {} 點血量".format(
            actor["name"], target["name"], damage, target["name"], target["health"]))

    def rollEvent(self, actor):
        """ 骰隨機事件 """
        pass

    def checkBattleEnd(self):
        """ 判斷戰鬥是否結束 """
        players = False
        enemy = False
        for actor in self.players:
            if(actor["health"] > 0):
                players = True
                break
        for actor in self.enemy:
            if(actor["health"] > 0):
                enemy = True
                break

        if(players and not enemy):
            self.isBattleEnd = True
            self.winner = "玩家"
        elif(not players and enemy):
            self.isBattleEnd = True
            self.winner = "敵"

    def getLog(self):
        """ 取得對戰紀錄 """
        return "\n".join(self.log)
