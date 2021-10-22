import importlib
import os

# * Envs
CMD_PREFIX = os.environ.get('PREFIX', '$')

async def cmd_resolver(bot):
  try:
    command_path = os.path.abspath(__file__)
    cogs_path = os.path.dirname(command_path)

    with os.scandir(f'{cogs_path}/cogs') as entries:
      for entry in entries:
        if entry.is_dir():
          continue

      cog_name = entry.name[:len(entry.name) - 3]
      cog = importlib.import_module(f'cogs.{cog_name}')

      cog_class = getattr(cog, cog_name)

      bot.add_cog(cog_class(bot))


  except ModuleNotFoundError as e:
    print(e)
