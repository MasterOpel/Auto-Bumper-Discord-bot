import discord
import threading

from discord.ext import tasks

@tasks.loop(seconds=1800)
async def auto_bump():
  while True:
    await client.channel.send('/bump')
    
started = False
token = input("Type your token here: ")
client = discord.Client()
thread = threading.Thread(target=auto_bump, daemon=True)
  
@client.event
async def on_ready():
  print('The bot initialized successfully!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global started
  if message.content.startswith('$start') and not started:
    client.channel = client.get_partial_messageable(message.channel.id, guild_id=message.channel.guild_id)
    auto_bump.start();
    await message.channel.send('The auto-bump operation was successfully started!')

client.run(token)
