import importlib
import os

# * Envs
CMD_PREFIX = os.environ.get('PREFIX', '$')

async def cmd_resolver(message, client):
  try:
    if not message.content.startswith(CMD_PREFIX):
      return

    args = message.content[len(CMD_PREFIX):].split(' ')
    command = args.pop(0)

    module = importlib.import_module(f'commands.{command}')

    function = getattr(module, command)
    await function(message, args, client)
  except ModuleNotFoundError:
    await message.channel.send('Comando no encontrado')
