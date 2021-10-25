from discord.ext import commands

import time


class Util(commands.Cog):
  def __init__(self, bot) -> None:
    self.bot = bot

  @commands.command()
  async def ping(self, ctx, ):
    '''Shows the message's ping'''

    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong 🏓 \n`ping took {int(ping)}ms`")
    print(f'Ping  {int(ping)}ms')


def setup(bot) -> None:
  bot.add_cog(Util(bot))
