import os
import dotenv
from logic.gameController import GameContoller


dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
gc = GameContoller()
discordId = 1

while(True):
    message = input("Action: ")
    if(message == "exit"):
        break

    if (message == "fight"):
        player = gc.create(discordId, "ToFuu")
        result = gc.battle(discordId)
        print(result)

    if(message == "find"):
        gc.findEnemy(discordId)
        result = gc.showEnemy(discordId)
        print(result)