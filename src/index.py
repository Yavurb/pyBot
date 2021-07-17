# Importing Modules
import discord
import os

# * Importing specific modules
from dotenv import load_dotenv
from cmd_resolver import *

# * load envs
load_dotenv()

# Envs
API_KEY = os.getenv('API_KEY')

def main():
  client = discord.Client()

  @client.event
  async def on_ready():
    print(f'Logged on as {client.user}')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    await cmd_resolver(message, client)

  client.run(API_KEY)

if __name__ == '__main__':
  main()