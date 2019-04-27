import traceback
import sys
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)
        
        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(f'Command not found! Use `!roms` to see available commands.')

        elif isinstance(error, commands.MissingRequiredArgument):
            print(error)
            return await ctx.send(f'What device? It should be `!{ctx.command} <device>`')

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'`!{ctx.command}` has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'`!{ctx.command}` cannot be used in private messages.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return await ctx.send("Couldn't find this member. Please try again.")
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))

