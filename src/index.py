# Importing Modules
from discord.ext import commands
import os

# * Importing specific modules
from bot_loader import *

# Envs
API_KEY = os.getenv('API_KEY')
CMD_PREFIX = os.getenv('CMD_PREFIX')

def main():
  bot = commands.Bot(command_prefix=CMD_PREFIX)

  @bot.event
  async def on_ready():
    print(f'Logged on as {bot.user}')
    await bot_loader(bot)

  @bot.event
  async def on_command_error(ctx, exception):
    print(exception)
    print(ctx)


  bot.run(API_KEY)

if __name__ == '__main__':
  main()