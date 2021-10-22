# Importing Modules
from discord.ext import commands
import os

# * Importing specific modules
from cmd_resolver import *

# Envs
API_KEY = os.getenv('API_KEY')
CMD_PREFIX = os.getenv('CMD_PREFIX')

def main():
  bot = commands.Bot(command_prefix=CMD_PREFIX)

  @bot.event
  async def on_ready():
    print(f'Logged on as {bot.user}')

  @bot.event
  async def on_message(message):
    if message.author == bot.user:
      return

    await cmd_resolver(message, bot)

  bot.run(API_KEY)

if __name__ == '__main__':
  main()