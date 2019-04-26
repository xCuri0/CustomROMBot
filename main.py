import discord
from discord.ext import commands
import os
import private_stuff

prefix = "!"

bot = commands.Bot(command_prefix=prefix)

startup_extensions = os.listdir("./cogs")
if "__pycache__" in startup_extensions:
    startup_extensions.remove("__pycache__")
startup_extensions = [ext.replace('.py', '') for ext in startup_extensions]
loaded_extensions = []

bot.remove_command("help")

roms = 'DotOS (dotos)\n' \
       'Evolution-X (evo)\n' \
       'HavocOS (havoc)\n' \
       'PearlOS (pearl)\n' \
       'PixysOS (pixy)\n' \
       'Potato Open Sauce Project (posp)\n' \
       'ViperOS (viper)\n' \
       'LineageOS (lineage)\n' \
       'PixelExperience (pe) \n'

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
    embed = discord.Embed(title="Custom ROM Bot help", description="Fetches latest builds from "
                                                                   "official devices", color=0x5eff72)
    embed.add_field(name="ROMs Available:", value=f"{roms}", inline=False)
    embed.add_field(name="Usage:", value=f"!(rom) (device) \nExample: !evo tissot\nYou can also view available roms"
                                         f" with {prefix}roms.", inline=False)
    embed.set_footer(text="bot was made by Keikei14 | Keikei14#7950")
    await ctx.send(embed=embed)


@bot.command(name="roms")
async def romcommand(ctx):
    embed = discord.Embed(title="ROMs Available:", description=f"{roms}", color=0x5eff72)
    embed.set_footer(text="bot was made by Keikei14 | Keikei14#7950")
    await ctx.send(embed=embed)

bot.run(private_stuff.token, bot=True, reconnect=True)