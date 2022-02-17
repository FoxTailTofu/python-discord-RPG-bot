import os
import discord
import dotenv
from game import Game

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
game = Game()


@client.event
async def on_ready():
    print(f'{client.user.name} 連線成功！')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.content == "TofuBot":
        await message.reply("嗨")
        return

    if message.content == "INIT":
        game.reset()
        await message.delete()
        await message.channel.send("===重設資料===\n" + game.showStatus())

    if message.content == "ATTACK":
        await message.delete()
        await message.channel.send("===攻擊回合===\n" + game.attack() + "\n===回合結束===\n" + game.check())

    if message.content == "HEAL":
        game.heal()
        await message.delete()
        await message.channel.send("===玩家嗑藥===\n" + game.player.showHealth())

client.run(TOKEN)
