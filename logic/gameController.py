
from logic.baseMobGenerator import baseMobGenberator
from logic.battleManager import battleManager
from logic.playerManager import playerManager


class GameContoller:
    """ 取得對應玩家和行為，遊戲基本邏輯都在這邊整合 """

    def __init__(self) -> None:
        self.playerManager = playerManager()
        self.mobGenerator = baseMobGenberator()

        pass

    def create(self, discordId, name):
        """ 建立新角色 """
        player = self.playerManager.find(discordId)
        if(player != None):
            return -1

        return self.playerManager.create(discordId, name)

    def battle(self, discordId):
        """ 進入戰鬥 """
        player = self.playerManager.find(discordId)
        if(player == None):
            return -1
        enemy = self.mobGenerator.create(player["level"])

        # 一個玩家對一個敵人
        bm = battleManager([player], [enemy])
        bm.main()
        print(bm.getLog())
