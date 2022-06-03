import discord

token = input("Type your token here: ")
client = discord.Client()

@client.event
async def on_ready():
  print('The bot initialized successfully!')
  
client.run(token)
