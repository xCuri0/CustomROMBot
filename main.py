import discord
from discord.ext import commands
import os
import private_stuff

prefix = ">."

bot = commands.Bot(command_prefix=prefix)

startup_extensions = os.listdir("./cogs")
if "__pycache__" in startup_extensions:
    startup_extensions.remove("__pycache__")
startup_extensions = [ext.replace('.py', '') for ext in startup_extensions]
loaded_extensions = []

bot.remove_command("help")


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    game = discord.Game("with you <3")
    await bot.change_presence(status=discord.Status.online, activity=game)

    print("Loading {} extension(s)...".format(len(startup_extensions)))

    for extension in startup_extensions:
        try:
            bot.load_extension("cogs.{}".format(extension.replace(".py", "")))
            loaded_extensions.append(extension)

        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n\t->{}'.format(extension, exc))
    print('Successfully loaded the following extension(s): {}'.format(loaded_extensions))


@bot.command()
async def help(ctx):
    message = "Commands:\n" \
              "dotos (device)\n" \
              "evo (device)\n" \
              "havoc (device)\n" \
              "pearl (device)\n" \
              "pixy (device)\n" \
              "posp (device)\n" \
              "posptest (device)\n" \
              "viper (device)\n" \
              "lineage (device)\n" \
              "miuifastboot (device) (china/india)\n" \
              "miuirecovery (device) (china/india)"
    await ctx.send(message)

bot.run(private_stuff.token, bot=True, reconnect=True)