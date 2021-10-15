# description => Shows the bot's commands
# options => []

import os
import json
from discord import Embed, Colour

async def help(message, args, client):
  command_path = os.path.abspath(__file__)
  dir_path = os.path.dirname(command_path)

  commands = []

  embed = Embed(title = 'Commands', colour = Colour.from_rgb(186, 85, 211))

  with os.scandir(dir_path) as files:
    for file in files:

      file_path = os.path.join(dir_path, file)

      with open(file_path, 'r') as opened_file:
        description = opened_file.readline().split('=>')[1].strip()
        options = opened_file.readline().split('=>')[1].strip()
        options = f'option: {", ".join(json.loads(options))}' if options != '[]' else ''

        name = file.name[:len(file.name) - 3]
        embed.add_field(name = name, value = description, inline = False)

  await message.channel.send(embed = embed)