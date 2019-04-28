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

    async def getbtlg(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://bootleggersrom-devices.github.io/api/devices.json") as devices:
                usr = await devices.json()
                if device not in usr:
                    await ctx.send('No builds for device :(')
                elif device in usr:
                    filesize = size(int(usr[device]['buildsize']))
                    valued = f"**Build date**: `{usr[device]['buildate']}`\n" \
                             f"**Size**: `{filesize}`\n" \
                             f"**Download**: [{usr[device]['filename']}]({usr[device]['download']})"
                    embed = discord.Embed(title=f"BootleggersROM | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)

    async def getaex(self, ctx, device, version):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.aospextended.com/ota/{device}/{version}') as fetch:
                usr = await fetch.json()
                if usr['error']:
                    return await ctx.send('No builds for device :(')
                elif not usr['error']:
                    filesize = size(usr['filesize'])
                    valued = f"**Build date**: `{usr['build_date']}`\n" \
                             f"**Size**: `{filesize}`\n" \
                             f"**Download**: [{usr['filename']}]({usr['url']})"
                    embed = discord.Embed(title=f"BootleggersROM | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)

    async def getpe(self, ctx, device, versionpe):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/{versionpe}') as fetch:
                usr = await fetch.json()
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
                    await ctx.send(f"No builds for device :(")

    async def getlos(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
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
                    elif str(usr['response']) == '[]':
                        await ctx.send('No builds for device :(')

    async def gethavoc(self, ctx, device):
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
                    await ctx.send("No builds for device :(")

    async def getpixys(self, ctx, device: str):
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
                    await ctx.send("No builds for device :(")

    async def getpearl(self, ctx, device):
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
                    return await ctx.send("No builds for device :(")

    async def getdotos(self, ctx, device):
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
                    return await ctx.send("No builds for device :(")

    async def getviper(self, ctx, device):
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
                    await ctx.send("No builds for device :(")

    async def getevo(self, ctx, device):
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

    async def getposp(self, ctx, device):
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
                        await ctx.send('No builds for device :(')
                else:
                    await ctx.send('No builds for device :(')

    @commands.command(aliases=['potato'])
    async def posp(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json()
                    if str(usr['response']) != "[]":
                        await self.getposp(ctx, device)
                    elif str(usr['response']) == '[]':
                        device = phone.upper()
                        await self.getposp(ctx, device)
                else:
                    await ctx.send('No builds for device :(')

    @commands.command(aliases=['evox'])
    async def evo(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json') as fetch:
                if fetch.status == 200:
                    await self.getevo(ctx, device)
                elif fetch.status == 404:
                    device = phone.upper()
                    await self.getevo(ctx, device)

    @commands.command()
    async def viper(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json') as fetch:
                if fetch.status == 200:
                    await self.getviper(ctx, device)
                elif fetch.status == 404:
                    device = phone.upper()
                    await self.getviper(ctx, device)
                else:
                    await ctx.send('Could not reach ViperOS servers.')

    @commands.command()
    async def dotos(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json') as fetch:
                if fetch.status == 200:
                    await self.getdotos(ctx, device)
                elif fetch.status == 404:
                    device = phone.upper()
                    await self.getdotos(ctx, device)

    @commands.command()
    async def pearl(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json') as fetch:
                if fetch.status == 200:
                    await self.getpearl(ctx, device)
                elif fetch.status == 404:
                    device = phone.upper()
                    await self.getpearl(ctx, device)
                else:
                    await ctx.send('Could not reach PearlOS servers.')

    @commands.command(aliases=['pixys'])
    async def pixy(self, ctx, phone):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
                if fetch.status == 404:
                    device = phone.upper()
                    await self.getpixys(ctx, device)
                elif fetch.status == 200:
                    await self.getpixys(ctx, device)
                else:
                    await ctx.send('Could not reach PixysOS servers.')

    @commands.command()
    async def havoc(self, ctx, phone):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json') as fetch:
                if fetch.status == 200:
                    await self.gethavoc(ctx, device)
                if fetch.status == 404:
                    device = phone.upper()
                    await self.gethavoc(ctx, device)

    @commands.command(aliases=['los', 'lineageos'])
    async def lineage(self, ctx, phone):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json()
                    if str(usr['response']) == '[]':
                        device = phone.upper()
                        await self.getlos(ctx, device)
                    elif str(usr['response']) != '[]':
                        await self.getlos(ctx, device)
                else:
                    await ctx.send('Cannot connect to LineageOS servers.')

    @commands.command()
    async def pe(self, ctx, phone, peversion=None):
        device = phone.lower()
        if peversion is None:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                    versionpe = 'pie'
                    usr = await fetch.json()
        elif peversion.lower() == 'caf':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                    versionpe = 'pie_caf'
                    usr = await fetch.json()
        elif peversion.lower() == 'oreo':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo') as fetch:
                    versionpe = 'oreo'
                    usr = await fetch.json()
        elif peversion.lower() == 'pie':
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                    versionpe = 'pie'
                    usr = await fetch.json()
        else:
            return await ctx.send('Device/Version not found!')
        if fetch.status == 200:
            if usr['error']:
                device = phone.upper()
                await self.getpe(ctx, device, versionpe)
            if not usr['error']:
                await self.getpe(ctx, device, versionpe)
        elif fetch.status == 404:
            await ctx.send('Could not reach Pixel Experience servers.')

    @commands.command(aliases=['btlg'])
    async def bootleggers(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://bootleggersrom-devices.github.io/api/devices.json") as devices:
                if devices.status == 200:
                    usr = await devices.json()
                    if device not in usr:
                        device = phone.upper()
                        await self.getbtlg(ctx, device)
                    elif device in usr:
                        await self.getbtlg(ctx, device)
                elif devices.status != 404:
                    await ctx.send("Couldn't reach Bootleggers API!")

    @commands.command()
    async def aex(self, ctx, phone: str, version='pie'):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.aospextended.com/ota/{device}/{version}') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json()
                    if usr['error']:
                        device = phone.upper()
                        await self.getaex(ctx, device, version)
                    elif not usr['error']:
                        await self.getaex(ctx, device, version)
                elif fetch.status == 404:
                    await ctx.send('Cannot connect to AEX servers.')
                elif fetch.status == 403:
                    device = phone.upper()
                    await self.getaex(ctx, device, version)


def setup(bot):
    bot.add_cog(ROMResolver(bot))
