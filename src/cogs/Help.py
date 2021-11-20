from discord import channel
from discord.ext import commands
import discord

class HelpCommand(commands.MinimalHelpCommand):
  def get_command_signature(self, command):
    return f'{command.qualified_name.capitalize()} {command.signature}'

  async def send_bot_help(self, mapping):
    embed = discord.Embed(title='Help', color=discord.Color.blue())

    for cog, commands in mapping.items():
      filtered = await self.filter_commands(commands, sort=True)
      command_signatures = [self.get_command_signature(c) for c in filtered]
      if command_signatures:
        cog_name = getattr(cog, 'qualified_name', "No Category")
        embed.add_field(name=cog_name, value='\n'.join(command_signatures), inline=False)

    channel = self.get_destination()
    await channel.send(embed=embed)

  async def send_command_help(self, command):
    embed = discord.Embed(title=self.get_command_signature(command), color=discord.Color.blue())
    embed.add_field(name='Description', value=command.help)

    channel = self.get_destination()
    await channel.send(embed=embed)



class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    help_command = HelpCommand()
    help_command.cog = self
    bot.help_command = help_command


def setup(bot):
  bot.add_cog(Help(bot))