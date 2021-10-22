from discord.ext import commands
from discord import Embed, Colour

import time
import os
import json

class Util(commands.Cog):
  def __init__(self, bot) -> None:
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong 🏓 \n`ping took {int(ping)}ms`")
    print(f'Ping  {int(ping)}ms')

  @commands.command()
  async def sh(self, ctx):
    command_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(command_path)

    commands = []

    embed = Embed(title = 'Commands', colour = Colour.from_rgb(186, 85, 211))

    with os.scandir(dir_path) as entries:
      for entry in entries:
        if entry.is_dir():
          continue

        entry_path = os.path.join(dir_path, entry)

        with open(entry_path, 'r') as opened_file:
          description = opened_file.readline().split('=>')[1].strip()
          options = opened_file.readline().split('=>')[1].strip()
          options = f'option: {", ".join(json.loads(options))}' if options != '[]' else ''

          name = entry.name[:len(entry.name) - 3]
          embed.add_field(name = name, value = description, inline = False)

    await ctx.send(embed = embed)