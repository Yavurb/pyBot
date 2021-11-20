import os

async def bot_loader(bot):
    for folder in os.listdir('./src/cogs'):
      try:
        if os.path.exists(os.path.join("./src/cogs", folder, "cog.py")):
          bot.load_extension(f"cogs.{folder}.cog")
      except Exception as e:
        print(f"{folder} failed to load: {e}")
