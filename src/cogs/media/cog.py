from discord.ext import commands


class Media(commands.Cog):
  """Multimedia commands"""

  def __init__(self, bot) -> None:
    self.bot = bot

  @commands.command()
  async def play(self, ctx: commands.Context, song: str):
    '''Shows the message's ping'''
    if not ctx.author.voice:
      await ctx.reply('You are not in a voice channle.')
      return

    voice_channel = ctx.author.voice.channel
    # await voice_channel.connect()


def setup(bot) -> None:
  bot.add_cog(Media(bot))
