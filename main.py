import discord
import requests
import random
import urllib.request
import cv2
import os


client = discord.Client()

def get_memes():
  j = requests.get("https://memeapi.pythonanywhere.com/memes+dankmemes+pewdiepiesubmissions/5").json()
  s = len(j) 
  r = random.randint(0,s)
  return j['memes'][r]['url']
def get_meme_template():
   
    j = requests.get("https://api.imgflip.com/get_memes").json()
    z = len(j)
    r = random.randint(0,z)
    return j['data']['memes'][r]['url']

@client.event
async def on_ready():
    print('Hi i am {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
        return
  
  if message.content.startswith('$help'):
    await message.channel.send("Commands for meme bot:")
    await message.channel.send("1.$meme For memes")
    await message.channel.send("2.$template for meme template")
  
  if message.content.startswith('$hello'):
        await message.channel.send('Hello')

  if message.content.startswith('$template'):
        meme_temp = get_meme_template()
        await message.channel.send(meme_temp)

  if message.content.startswith('$meme'):
        meme = get_memes()
        await message.channel.send(meme)
    

client.run(os.getenv('Token'))
