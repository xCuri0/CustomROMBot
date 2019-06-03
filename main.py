import discord
from discord.ext import commands
import os
import asyncio
import sys

prefix = "!"

bot = commands.Bot(command_prefix=prefix, case_insensitive=True, owner_id=177426944063700995)

startup_extensions = os.listdir("./cogs")
if "__pycache__" in startup_extensions:
    startup_extensions.remove("__pycache__")
startup_extensions = [ext.replace('.py', '') for ext in startup_extensions]
loaded_extensions = []

bot.remove_command("help")

roms = 'AOSP Extended (aex/aospextended) \n' \
       'Android Open Source illusion Project (aosip/illusion)\n' \
       'BootleggersROM (btlg/bootleggers) \n' \
       'crDroid (crdroid)\n' \
       'DotOS (dotos/dot)\n' \
       'Evolution-X (evo/evox/evolutionx)\n' \
       'HavocOS (havoc/havocos)\n' \
       'LineageOS (los/lineage)\n' \
       'PearlOS (pearl/pearlos)\n' \
       'Pixel Experience (pe/pixelexperience) \n' \
       'PixysOS (pixy/pixys/pixysos)\n' \
       'Potato Open Sauce Project (posp/potato/potatorom)\n' \
       'Resurrection Remix (rr/resurrection/resurrectionremix/resurrectionremixos/rros)\n' \
       'RevengeOS(revenge/revengeos)\n' \
       'SuperiorOS(superior/superioros)\n' \
       'Syberia (syberia)\n' \
       'ViperOS (viper/viperos)\n'


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
    embed = discord.Embed(title="Custom ROM Bot", description="Fetches the latest builds of "
                                                              "officially supported devices", color=0x5eff72)
    embed.add_field(name="Available ROMs", value=f"{roms}\nYou can also view available ROMs with `{prefix}roms`.", inline=False)
    embed.add_field(name="Usage", value=f"`!<rom> <device>` \n"
                                         f"Example: `!evo tissot`\n"
                                         f"To see available ROMs for a device, use `{prefix}roms <device>`.\n"
                                         , inline=False)
    embed.add_field(name="For Pixel Experience and AEX", value="`!pe <device> <version>`\n"
                                                               "Versions: Oreo (oreo), Pie (pie), "
                                                               "Pie-CAF (caf) (exclusive to PE)\n"
                                                               "Example: `!pe tissot oreo`", inline=False)
    embed.add_field(name='Magisk', value='gets latest Magisk version (stable/canary/beta)\n'
                                         'Usage: `!magisk (beta/canary/stable)`')
    embed.add_field(name='OpenGAPPS', value='gets latest OpenGAPPS build\n'
                                            'Usage: `!gapps (arch) (android version) (gapps variant)`')
    embed.set_footer(text="Bot by Keikei14 | Keikei14#7950")
    try:
        await ctx.author.send(embed=embed)
    except:
        await ctx.send(f'Oh no! I can\'t DM {ctx.author.name}!')


@bot.command()
@commands.is_owner()
async def say(ctx, *, message):
    if "@everyone" in message or "@here" in message or ctx.message.mention_everyone:
        return await ctx.message.delete()
    else:
        await ctx.message.delete()
        await ctx.send(message)


@bot.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send(f'{bot.user.name} is restarting...')
    os.execl(sys.executable, sys.executable, *sys.argv)

bot.run(os.environ['token'], bot=True, reconnect=True)
