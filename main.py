from mymodules import wish_hbd,getJsonData
from boto.s3.connection import S3Connection

import discord
import datetime,os
from discord.ext import tasks,commands

bot = commands.Bot(command_prefix='$' ,intents=discord.Intents.all())


@bot.event
async def on_ready():
    send_wishes.start()
    print(f"logged in as {bot.user}")

@tasks.loop(hours=1)
async def send_wishes():
    
    # Opening the JSON file (data.json) in read only mode.
    data_file = open("data.json", "r")
    namev =[]
    await bot.wait_until_ready()
    
    while True:
        try:
            # to get current date
            datt = datetime.datetime.now()
            namev = getJsonData(data_file, "name", "birth_month", "birth_date",str(datt.month), str(datt.day))
        except:
            continue
        if namev !=[]:
            message_channel=bot.get_channel(1025458220912869389)
            for name in namev:
                await message_channel.send(wish_hbd(name))
            break
            


bot.run(S3Connection(os.environ['TOKEN']))