import discord
import time
import threading

def auto_bump():
  global channel
  while True:
    channel.send('/bump')
    time.sleep(1800)
    
started = False
token = input("Type your token here: ")
client = discord.Client()
channel = None;
thread = threading.Thread(auto_bump, daemon=True, group=None)
    
def on_start():
  global started
  thread.start()
  started = True

def on_stop():
  global started
  thread.stop()
  started = False
  
@client.event
async def on_ready():
  print('The bot initialized successfully!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global started
  if message.content.startswith('$start') and not started:
    global channel
    on_start()
    channel = message.channel
    await message.channel.send('The auto-bump operation was successfully started!')

  if message.content.startswith('$stop') and started:
    on_stop()
    await message.channel.send('The auto-bump operation was successfully stopped!')

client.run(token)
