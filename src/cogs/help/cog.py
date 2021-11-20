from discord.ext import commands
from .help_command import HelpCommand

class Help(commands.Cog):
  """Shows a brief summary of commands ordered by category"""

  def __init__(self, bot):
    bot._original_help_command = bot.help_command
    bot.help_command = HelpCommand()
    bot.help_command.cog = self


def setup(bot):
  bot.add_cog(Help(bot))