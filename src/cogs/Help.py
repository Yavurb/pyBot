from typing import Optional, Set
from discord import Embed
from discord.ext import commands



class HelpCommand(commands.MinimalHelpCommand):
  def get_command_signature(self, command):
    signature = f' {command.signature}' if command and command.signature else ''
    return f'`{self.clean_prefix}{command.qualified_name}{signature}`'


  async def _help_embed(
    self, title: str, description: Optional[str] = None, mapping: Optional[dict] = None,
    command_set: Optional[Set[commands.Command]] = None, set_author: bool = True
  ):
    embed = Embed(title=title)

    if set_author:
      avatar = self.context.bot.user.avatar_url or self.context.bot.user.default_avatar_url
      embed.set_author(name=self.context.bot.user.name, icon_url=avatar)

    if description:
      embed.description = description

    if command_set:
      #Show help about all commands in the set
      filtered = await self.filter_commands(command_set, sort=True)
      if filtered:
        for command in filtered:
          embed.add_field(
            name=self.get_command_signature(command),
            value=command.short_doc or '...',
            inline=False
          )

    if mapping:
      # Add a short description of commands in each cog.
      for cog, commands in mapping.items():
        filtered = await self.filter_commands(commands, sort=True)
        if filtered:
          cog_name = getattr(cog, 'qualified_name', "No Category")
          cmd_list = '\u2002'.join(
            f'`{self.clean_prefix}{command.name}`' for command in filtered
          )

          value = (
            f'{cog.description}\n{cmd_list}'
            if cog and cog.description
            else cmd_list
          )

          embed.add_field(name=cog_name, value=value)

    return embed


  async def send_bot_help(self, mapping: dict):
    embed = await self._help_embed(
      title='Bot Commands',
      description=self.context.bot.description,
      mapping=mapping
    )
    channel = self.get_destination()
    await channel.send(embed=embed)


  async def send_command_help(self, command: commands.Command):
    embed = await self._help_embed(
      title=f'{command.name.capitalize()} Command',
      description=command.help,
      command_set=command.commands if isinstance(command, commands.Group) else None
    )
    channel = self.get_destination()
    await channel.send(embed=embed)


  async def send_cog_help(self, cog: commands.Cog):
    embed = await self._help_embed(
      title=f'{cog.qualified_name}',
      description=cog.description,
      command_set=cog.get_commands()
    )
    channel = self.get_destination()
    await channel.send(embed=embed)

  send_group_help = send_command_help


class Help(commands.Cog):
  def __init__(self, bot):
    bot._original_help_command = bot.help_command
    bot.help_command = HelpCommand()
    bot.help_command.cog = self


def setup(bot):
  bot.add_cog(Help(bot))