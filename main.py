# import os
# import dotenv

# dotenv.load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# while(True):
#     message = input("Action: ")

#     if(message == "exit"):
#         break


from logic.gameController import GameContoller


gc = GameContoller()
player = gc.create(1,"ToFuu")
gc.battle(1)