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
thread = threading.Thread(target=auto_bump, daemon=True)
    
def on_start():
  global started, thread
  thread.start()
  started = True

def on_stop():
  global started, thread
  thread._stop()
  started = False
  
@client.event
async def on_ready(self):
  print('The bot initialized successfully!')
  print(f'Logged in as {self.user} (ID: {self.id})')

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
