import os

async def help(message, args, client):
  file_path = os.path.abspath(__file__)
  dir_path = os.path.dirname(file_path)

  filenames = os.listdir(dir_path)

  commands = []
  for file in filenames:
    name = file.split('.')[0]
    commands.append(name)

  await message.channel.send('commands: \n'+'\n'.join(commands))