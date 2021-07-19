from os import listdir
from os import walk
from pathlib import Path

async def help(message, args, client):
  command_path = Path(__file__).parent.resolve()
  (_,_, filenames) = walk(command_path).__next__()

  commands = []
  for file in filenames:
    name = file.split('.')[0]
    commands.append(name)

  await message.channel.send('commands: \n'+'\n'.join(commands))