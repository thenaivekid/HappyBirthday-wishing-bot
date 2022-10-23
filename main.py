from unicodedata import name
import discord 
from decouple import config
import json
import datetime
from discord.ext import tasks

client = discord.Client(intents=discord.Intents.all())

# function returns text to send 
def wish_hbd(name):
    return f"@everyone \nHappy Birthday to you, {name}"

# This function returns a list of values 
# based on conditions on moneth and day from the JSON file.
# use to return names of members having their birthday on current date.
def getJsonData(file, name, birth_month, birth_date, current_month, current_date):
     
    # Load the file's data in 'data' variable
    data = json.load(file)
    retv =[]
 
    # If the attributes' value conditions are satisfied,
    # append the name into the list to be returned.
    for i in data:
        if(i[birth_month]== current_month and i[birth_date]== current_date):
           retv.append(i[name])
    return retv
 
# Opening the JSON file (data.json) in read only mode.
data_file = open("data.json", "r")
namev =[]
print("Script Running")
 
# This will keep rerunning the part of
# the code from 'while True' to 'break'.
# use to keep waiting for the JSON function
# to return a non empty list.
# In practice, this function will keep rerunning at
# 11:59pm a day before the birthday and break out at 12:00am.

@client.event
async def on_ready():
    print(f"logged in as {client.user}")


async def send_wishes():
    message_channel_id= '1025458220912869389' #channel ID to send 
    await client.wait_until_ready()
    message_channel=client.get_channel(message_channel_id)
    while True:
        try:
            # to get current date
            datt = datetime.datetime.now()
            namev = getJsonData(data_file, "name", "birth_month", "birth_date",str(datt.month), str(datt.day))
        except:
            continue
        if namev !=[]:
            message_channel.send(wish_hbd(namev))
            
send_wishes()
client.run(config('TOKEN'))