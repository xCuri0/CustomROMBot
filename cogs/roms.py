from discord.ext import commands
from hurry.filesize import size
import discord
from datetime import date
import aiohttp

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950"


class ROMResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def posp(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json()
                    if str(usr['response']) != "[]":
                        builddate = date.fromtimestamp(usr['response'][-1]['datetime'])
                        filesize = size(int(usr['response'][-1]['size']))
                        valued = f"**Build Date**: `{builddate}`\n" \
                                 f"**Size**: `{filesize}`\n" \
                                 f"**Version**: `{usr['response'][-1]['version']}`\n" \
                                 f"**Download**: [{usr['response'][-1]['filename']}]({usr['response'][-1]['url']})"
                        embed = discord.Embed(title=f"Potato Open Sauce Project | {device}",
                                              description=valued,
                                              color=embedcolor)
                        embed.set_footer(text=embedfooter)
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send('Device not found!')
                else:
                    await ctx.send('Device not found!')

    @commands.command()
    async def evo(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['size']))
                    builddate = date.fromtimestamp(usr['datetime'])
                    valued = f"**Build date**: `{builddate}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Version**: `{usr['version']}`\n" \
                        f"**Download**: [{usr['filename']}]({usr['url']})"
                    embed = discord.Embed(title=f"Evolution-X | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("Device not found!")

    @commands.command()
    async def viper(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(int(usr['response'][0]['datetime']))
                    valued = f"**Build date**: `{builddate}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Version**: `{usr['response'][0]['version']}`\n" \
                        f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"ViperOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("Device not found!")

    @commands.command()
    async def dotos(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(usr['response'][0]['datetime'])
                    valued = f"**Build date**: `{builddate}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Version**: `{usr['response'][0]['version']}`\n" \
                        f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"DotOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    return await ctx.send("Device not found!")

    @commands.command()
    async def pearl(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(usr['response'][0]['datetime'])
                    valued = f"**Build date**: `{builddate}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Version**: `{usr['response'][0]['version']}`\n" \
                        f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"PearlOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    return await ctx.send("Device not found!")

    @commands.command()
    async def pixy(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(int(usr['response'][0]['datetime']))
                    valued = f"**Build date**: `{builddate}`\n" \
                             f"**Size**: `{filesize}`\n" \
                             f"**Version**: `{usr['response'][0]['version']}`\n" \
                             f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"PixysOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("Device not found!")

    @commands.command()
    async def havoc(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(usr['response'][0]['datetime'])
                    valued = f"**Build date**: `{builddate}`\n" \
                             f"**Size**: `{filesize}`\n" \
                             f"**Version**: `{usr['response'][0]['version']}`\n" \
                             f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"HavocOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("Device not found!")

    @commands.command(aliases=['los'])
    async def lineage(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json()
                    if str(usr['response']) != "[]":
                        filesize = size(usr['response'][0]['size'])
                        builddate = date.fromtimestamp(usr['response'][-1]['datetime'])
                        valued = f"**Build date**: `{builddate}`\n" \
                                 f"**Size**: `{filesize}`\n" \
                                 f"**Version**: `{usr['response'][-1]['version']}`\n" \
                                 f"**Download**: [{usr['response'][-1]['filename']}]({usr['response'][-1]['url']})"
                        embed = discord.Embed(title=f"LineageOS | {device}",
                                              description=valued,
                                              color=embedcolor)
                        embed.set_footer(text=embedfooter)
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send('Device not found!')
                else:
                    await ctx.send('Device not found!')

    @commands.command()
    async def pe(self, ctx, device, peversion=None):
        if peversion is None:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                    usr = await fetch.json()
        elif peversion.lower() == 'caf':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                    usr = await fetch.json()
        elif peversion.lower() == 'pie-caf':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                    usr = await fetch.json()
        elif peversion.lower() == 'pie_caf':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                    usr = await fetch.json()
        elif peversion.lower() == 'oreo':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo') as fetch:
                    usr = await fetch.json()
        elif peversion.lower() == 'pie':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                    usr = await fetch.json()
        else:
            return await ctx.send('Device/Version not found!')
        if not usr['error']:
            filesize = size(usr['size'])
            builddate = date.fromtimestamp(usr['datetime'])
            valued = f"**Build date**: `{builddate}`\n" \
                     f"**Size**: `{filesize}`\n" \
                     f"**Version**: `{usr['version']}`\n" \
                     f"**Download**: [{usr['filename']}]({usr['url']})"
            embed = discord.Embed(title=f"Pixel Experience | {device}",
                                  description=valued,
                                  color=embedcolor)
            embed.set_footer(text=embedfooter)
            await ctx.send(embed=embed)
        elif usr['error']:
            await ctx.send("Device/version not found!")

    @commands.command(aliases=['btlg'])
    async def bootleggers(self, ctx, device: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://bootleggersrom-devices.github.io/api/devices.json") as devices:
                if devices.status == 200:
                    usr = await devices.json()
                    if device in usr:
                        filesize = size(int(usr[device]['buildsize']))
                        valued = f"**Build date**: `{usr[device]['buildate']}`\n" \
                                 f"**Size**: `{filesize}`\n" \
                                 f"**Download**: [{usr[device]['filename']}]({usr[device]['download']})"
                        embed = discord.Embed(title=f"BootleggersROM | {device}",
                                              description=valued,
                                              color=embedcolor)
                        embed.set_footer(text=embedfooter)
                        await ctx.send(embed=embed)
                    else:
                        await ctx.send('Device not found!')
                elif devices.status == 404:
                    await ctx.send("Couldn't reach Bootleggers API!")


def setup(bot):
    bot.add_cog(ROMResolver(bot))
