from discord.ext import commands
from hurry.filesize import size
import discord
from datetime import date
import aiohttp

embedcolor = 0x5eff72
embedfooter = "bot was made by Keikei14 | Keikei14#7950"


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
                        valued = f"[{usr['response'][-1]['filename']}]({usr['response'][-1]['url']})\n" \
                                 f"Build Date: {builddate}\n" \
                                 f"Build Size: {filesize}\n" \
                                 f"Version: {usr['response'][-1]['version']}"
                        embed = discord.Embed(title="Potato Open Sauce Project Latest Build:",
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
                    valued = f"[{usr['filename']}]({usr['url']})\n" \
                        f"Build date: {builddate}\n" \
                        f"Build Size: {filesize}\n" \
                        f"Version: {usr['version']}"
                    embed = discord.Embed(title="Evolution-X Latest Build",
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
                    valued = f"[{usr['response'][0]['filename']}]({usr['response'][0]['url']})\n" \
                        f"Build date: {builddate}\n" \
                        f"Build size: {filesize}\n" \
                        f"Version: {usr['response'][0]['version']}"
                    embed = discord.Embed(title="ViperOS Latest Build:",
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
                    valued = f"[{usr['response'][0]['filename']}]({usr['response'][0]['url']})\n" \
                        f"Build date: {builddate}\n" \
                        f"Build size: {filesize}\n" \
                        f"Version: {usr['response'][0]['version']}"
                    embed = discord.Embed(title="DotOS Latest Build:",
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
                    valued = f"[{usr['response'][0]['filename']}]({usr['response'][0]['url']})\n" \
                        f"Build date: {builddate}\n" \
                        f"Build size: {filesize}\n" \
                        f"Version: {usr['response'][0]['version']}"
                    embed = discord.Embed(title="PearlOS Latest Build:",
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
                    valued = f"[{usr['response'][0]['filename']}]({usr['response'][0]['url']})\n" \
                             f"Build date: {builddate}\n" \
                             f"Build size: {filesize}\n" \
                             f"Version: {usr['response'][0]['version']}"
                    embed = discord.Embed(title="PixysOS Latest Build",
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
                    valued = f"[{usr['response'][0]['filename']}]({usr['response'][0]['url']})\n" \
                             f"Build date: {builddate}\n" \
                             f"Build size: {filesize}\n" \
                             f"Version: {usr['response'][0]['version']}"
                    embed = discord.Embed(title="HavocOS Latest Build",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("Device not found!")

    @commands.command()
    async def lineage(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json()
                    if str(usr['response']) != "[]":
                        filesize = size(usr['response'][0]['size'])
                        builddate = date.fromtimestamp(usr['response'][-1]['datetime'])
                        valued = f"[{usr['response'][-1]['filename']}]({usr['response'][-1]['url']})\n" \
                                 f"Build date: {builddate}\n" \
                                 f"Build size: {filesize}\n" \
                                 f"Version: {usr['response'][-1]['version']}"
                        embed = discord.Embed(title="LineageOS Latest Build",
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
            valued = f"[{usr['filename']}]({usr['url']})\n" \
                     f"Build date: {builddate}\n" \
                     f"Build size: {filesize}\n" \
                     f"Version: {usr['version']}"
            embed = discord.Embed(title="PixelExperience Latest Build",
                                  description=valued,
                                  color=embedcolor)
            embed.set_footer(text=embedfooter)
            await ctx.send(embed=embed)
        elif usr['error']:
            await ctx.send("Device/Version not found!")


def setup(bot):
    bot.add_cog(ROMResolver(bot))
