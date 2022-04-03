
import math
from random import random
from collections import defaultdict
from logic.baseMobGenerator import baseMobGenberator
from logic.battleManager import battleManager
from logic.playerManager import playerManager


class GameContoller:
    """ 取得對應玩家和行為，遊戲基本邏輯都在這邊整合 """

    def __init__(self):
        self.playerManager = playerManager()
        self.mobGenerator = baseMobGenberator()
        self.enemyList = defaultdict()
        pass

    def create(self, discordId, name):
        """ 建立新角色 """
        player = self.playerManager.find(discordId)
        if(player != None):
            return -1

        return self.playerManager.create(discordId, name)

    def findEnemy(self, discordId):
        player = self.playerManager.find(discordId)
        self.enemyList[discordId] = []
        for i in range(0,math.floor(random()*3)+1):
            enemy = self.mobGenerator.create(player["level"])
            self.enemyList[discordId].append(enemy)
        return self.enemyList[discordId]

    def showEnemy(self,discordId):
        enemies = self.enemyList[discordId]
        if(enemies == None):
            return "Nothing"
        result = ""
        for enemy in enemies:
            result += enemy['name'] + " Lv." + str(enemy['level']) +", "
        
        return result

    def battle(self, discordId):
        """ 進入戰鬥 """
        player = self.playerManager.find(discordId)
        enemies = self.enemyList.get(discordId)
        if(player == None or enemies == None):
            return -1
        bm = battleManager([player], enemies)
        bm.main()
        self.enemyList[discordId] = None
        return bm.getLog()
