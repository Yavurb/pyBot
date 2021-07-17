import importlib

async def cmd_resolver(message, client):
  try:
    if not message.content.startswith('>'):
      return

    command = message.content.split('>')[1];

    module = importlib.import_module(f'commands.{command}')

    function = getattr(module, command)
    await function(message)
  except ModuleNotFoundError:
    await message.channel.send('Comando no encontrado')
