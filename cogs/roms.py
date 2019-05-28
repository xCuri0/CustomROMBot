from discord.ext import commands
from hurry.filesize import size
import discord
from datetime import date
import aiohttp
import lxml
from bs4 import BeautifulSoup
import asyncio

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950"


class ROMResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def getsuperior(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/SuperiorOS/official_devices/pie/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(int(usr['response'][0]['datetime']))
                    valued = f"**Build date**: `{builddate}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Version**: `{usr['response'][0]['version']}`\n" \
                        f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"SuperiorOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("No builds for device <:harold:498881491368017930>")

    async def getrevenge(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/RevengeOS/releases/master/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    valued = f"**Build date**: `{usr[-1]['date']}`\n" \
                             f"**Size**: `{usr[-1]['size']}`\n" \
                             f"**Version**: `{usr[-1]['version']}`\n" \
                             f"**Download**: [{usr[-1]['file_name']}](https://acc.dl.osdn.jp/storage/g/r/re/revengeos/{device}/{usr[-1]['file_name']})"
                    embed = discord.Embed(title=f"RevengeOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("No builds for device <:harold:498881491368017930>")

    async def getrr(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://raw.githubusercontent.com/ResurrectionRemix-Devices/api/master/{device}.json') as fetch:
                if fetch.status == 200:
                    usr = await fetch.json(content_type=None)
                    filesize = size(int(usr['response'][0]['size']))
                    builddate = date.fromtimestamp(int(usr['response'][0]['datetime']))
                    valued = f"**Build date**: `{builddate}`\n" \
                             f"**Size**: `{filesize}`\n" \
                             f"**Version**: `{usr['response'][0]['version']}`\n" \
                             f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"Resurrection Remix | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("No builds for device <:harold:498881491368017930>")

    async def getsyberia(self, ctx, device, usr, partition):
        if partition == 'a-only':
            valued = f"**Build date**: `{usr['build_date']}`\n" \
                     f"**Download**: [{usr['filename']}]({usr['url']})"
            embed = discord.Embed(title=f"Syberia | {device}",
                                  description=valued,
                                  color=embedcolor)
            embed.set_footer(text=embedfooter)
            await ctx.send(embed=embed)
        elif partition == 'ab':
            filesize = size(int(usr['response'][0]['size']))
            builddate = date.fromtimestamp(usr['response'][0]['datetime'])
            valued = f"**Build date**: `{builddate}`\n" \
                     f"**Size**: `{filesize}`\n" \
                     f"**Version**: `{usr['response'][0]['version']}`\n" \
                     f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
            embed = discord.Embed(title=f"Syberia | {device}",
                                  description=valued,
                                  color=embedcolor)
            embed.set_footer(text=embedfooter)
            await ctx.send(embed=embed)

    async def getcrdroid(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    'https://raw.githubusercontent.com/crdroidandroid/android_vendor_crDroidOTA/9.0/update.xml') as fetch:
                if fetch.status == 200:
                    fetchawait = await fetch.read()
                    soup = BeautifulSoup(fetchawait.decode('utf-8'), features="lxml")
                    finddevice = soup.find(device)
                    if finddevice is not None:
                        valued = f"**Download**: [{finddevice.filename.contents[0]}]({finddevice.download.contents[0]})"
                        embed = discord.Embed(title=f"crDroid | {device}",
                                              description=valued,
                                              color=embedcolor)
                        embed.set_footer(text=embedfooter)
                        await ctx.send(embed=embed)
                    elif finddevice is None:
                        await ctx.send('Cannot find device. <:harold:498881491368017930>')
                else:
                    return ctx.send('Cannot connect to crDroid servers. <:harold:498881491368017930>')

    async def getbtlg(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://bootleggersrom-devices.github.io/api/devices.json") as devices:
                usr = await devices.json()
                filename = usr[device]['filename']
                splitname = filename.split('-')
                for i in splitname:
                    if i.startswith('20'):
                        date = i
                if device not in usr:
                    await ctx.send('No builds for device. <:harold:498881491368017930>')
                elif device in usr:
                    valued = f"**Build date**: `{date}`\n" \
                             f"**Download**: [{usr[device]['filename']}]({usr[device]['download']})"
                    embed = discord.Embed(title=f"BootleggersROM | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)

    async def getaex(self, ctx, device, version):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.aospextended.com/ota/{device}/{version}') as fetch:
                usr = await fetch.json(content_type=None)
                if usr['error']:
                    return await ctx.send('No builds for device. <:harold:498881491368017930>')
                elif not usr['error']:
                    filesize = size(usr['filesize'])
                    valued = f"**Build date**: `{usr['build_date']}`\n" \
                             f"**Size**: `{filesize}`\n" \
                             f"**Download**: [{usr['filename']}]({usr['url']})"
                    embed = discord.Embed(title=f"AEX | {device}",
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
                    await ctx.send(f"No builds for device <:harold:498881491368017930>")

    async def getlos(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                    usr = await fetch.json()
                    if str(usr['response']) != "[]":
                        filesize = size(usr['response'][-1]['size'])
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
                        await ctx.send('No builds for device <:harold:498881491368017930>')

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
                    await ctx.send("No builds for device <:harold:498881491368017930>")

    async def getpixys(self, ctx, device: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
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
                    await ctx.send("No builds for device <:harold:498881491368017930>")

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
                    return await ctx.send("No builds for device <:harold:498881491368017930>")

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
                    try:
                        filesize = size(int(usr['size']))
                        builddate = date.fromtimestamp(int(usr['datetime']))
                        valued = f"**Build date**: `{builddate}`\n" \
                            f"**Size**: `{filesize}`\n" \
                            f"**Version**: `{usr['version']}`\n" \
                            f"**Download**: [{usr['filename']}]({usr['url']})"
                    except KeyError:
                        filesize = size(int(usr['response'][0]['size']))
                        builddate = date.fromtimestamp(int(usr['response'][0]['datetime']))
                        valued = f"**Build date**: `{builddate}`\n" \
                            f"**Size**: `{filesize}`\n" \
                            f"**Version**: `{usr['response'][0]['version']}`\n" \
                            f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    except Exception as e:
                        print('from getviper:')
                        print(e)
                    embed = discord.Embed(title=f"ViperOS | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                elif fetch.status == 404:
                    await ctx.send("No builds for device <:harold:498881491368017930>")

    async def getevo(self, ctx, device):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/evolution-x-devices/official_devices/master/builds/{device}.json') as fetch:
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
                    await ctx.send("Device not found! <:harold:498881491368017930>")

    #async def getposp(self, ctx, device, channel='weekly'):
        #async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            #try:
                #async with session.get(f'https://api.potatoproject.co/checkUpdate?device={device}&type={channel}') as fetch:
                    #usr = await fetch.json()
                    #downloadlink = usr['response'][-1]['url']
            #except aiohttp.ClientConnectionError:
                #async with session.get(
                        #f'http://api.strangebits.co.in/checkUpdate?device={device}&type={channel}') as fetch:
                    #usr = await fetch.json()
                    #if channel == 'mashed':
                        #downloadlink = f"https://mirror.sidsun.com/__private__/{device}/{usr['response'][-1]['filename']}"
                    #else:
                        #downloadlink = f"https://mirror.sidsun.com/{device}/{usr['response'][-1]['filename']}"
            #if str(usr['response']) != "[]":
                #builddate = date.fromtimestamp(usr['response'][-1]['datetime'])
                #filesize = size(int(usr['response'][-1]['size']))
                #valued = f"**Build Date**: `{builddate}`\n" \
                         #f"**Size**: `{filesize}`\n" \
                         #f"**Version**: `{usr['response'][-1]['version']}`\n" \
                         #f"**Download**: [{usr['response'][-1]['filename']}]({downloadlink})"
                #embed = discord.Embed(title=f"Potato Open Sauce Project | {device}",
                                      #description=valued,
                                      #color=embedcolor)
                #embed.set_footer(text=embedfooter)
                #await ctx.send(embed=embed)
            #else:
                #await ctx.send('No builds for device <:harold:498881491368017930>')

    async def getaosip(self, ctx, device, version):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://aosip.dev/{device}/{version}') as fetch:
                usr = await fetch.json()
                if fetch.status == 200 and str(usr['response']) != '':
                    builddate = date.fromtimestamp(usr['response'][0]['datetime'])
                    filesize = size(int(usr['response'][0]['size']))
                    valued = f"**Build Date**: `{builddate}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Version**: `{usr['response'][0]['version']}`\n" \
                        f"**Download**: [{usr['response'][0]['filename']}]({usr['response'][0]['url']})"
                    embed = discord.Embed(title=f"AOSiP | {device}",
                                          description=valued,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send('No builds for device <:harold:498881491368017930>')

    #@commands.command(aliases=['potato'])
    #async def posp(self, ctx, phone: str, channel='weekly'):
        #device = phone.lower()
        #async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            #try:
                #async with session.get(f'https://api.potatoproject.co/checkUpdate?device={device}&type={channel}') as fetch:
                    #usr = await fetch.json()
            #except aiohttp.ClientConnectionError:
                #async with session.get(f'http://api.strangebits.co.in/checkUpdate?device={device}&type={channel}') as fetch:
                    #usr = await fetch.json()
            #if str(usr['response']) != "[]":
                #await self.getposp(ctx, device, channel)
            #elif str(usr['response']) == '[]':
                #device = phone.upper()
                #await self.getposp(ctx, device, channel)

    @commands.command(aliases=['evox'])
    async def evo(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/evolution-x-devices/official_devices/master/builds/{device}.json') as fetch:
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
                    await ctx.send('Could not reach ViperOS servers. <:harold:498881491368017930>')

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
                    await ctx.send('Could not reach PearlOS servers. <:harold:498881491368017930>')

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
                    await ctx.send('Could not reach PixysOS servers. <:harold:498881491368017930>')

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
                    await ctx.send('Cannot connect to LineageOS servers. <:harold:498881491368017930>')

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
            return await ctx.send('Device/Version not found! <:harold:498881491368017930>')
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
                    await ctx.send("Couldn't reach Bootleggers API! <:harold:498881491368017930>")

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
                    await ctx.send('Cannot connect to AEX servers. <:harold:498881491368017930>')
                elif fetch.status == 403:
                    device = phone.upper()
                    await self.getaex(ctx, device, version)

    @commands.command()
    async def crdroid(self, ctx, phone: str):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get('https://raw.githubusercontent.com/crdroidandroid/android_vendor_crDroidOTA/9.0/update.xml') as fetch:
                if fetch.status == 200:
                    fetchawait = await fetch.read()
                    soup = BeautifulSoup(fetchawait.decode('utf-8'), features="lxml")
                    finddevice = soup.find(device)
                    if finddevice is not None:
                        await self.getcrdroid(ctx, device)
                    elif finddevice is None:
                        device = phone.upper()
                        await self.getcrdroid(ctx, device)
                else:
                    ctx.send('Cannot connect to crDroid servers. <:harold:498881491368017930>')

    @commands.command()
    async def syberia(self, ctx, phone, partition="a-only"):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            if device == 'enchilada':
                partition = 'ab'
                device = 'OnePlus6'
                async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/{partition}/{device}.json') as fetch:
                    usr = await fetch.json(content_type=None)
                    await self.getsyberia(ctx, device, usr, partition)
            elif device == 'fajita':
                partition = 'ab'
                device = 'OnePlus6T'
                async with session.get(
                        f'https://raw.githubusercontent.com/syberia-project/official_devices/master/{partition}/{device}.json') as fetch:
                    usr = await fetch.json(content_type=None)
                    await self.getsyberia(ctx, device, usr, partition)
            else:
                async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/{partition}/{device}.json') as fetch:
                    if fetch.status == 404:
                        partition = 'ab'
                        async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/{partition}/{device}.json') as fetch:
                            if fetch.status == 404:
                                await ctx.send('Cannot find device <:harold:498881491368017930>')
                            elif fetch.status == 200:
                                usr = await fetch.json(content_type=None)
                                await  self.getsyberia(ctx, device, usr, partition)
                    elif fetch.status == 200:
                        usr = await fetch.json(content_type=None)
                        await self.getsyberia(ctx, device, usr, partition)

    @commands.command()
    async def rr(self, ctx, phone):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://raw.githubusercontent.com/ResurrectionRemix-Devices/api/master/{device}.json') as fetch:
                if fetch.status == 404:
                    device = phone.upper()
                    await self.getrr(ctx, device)
                elif fetch.status == 200:
                    await self.getrr(ctx, device)

    @commands.command()
    async def revenge(self, ctx, phone):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://raw.githubusercontent.com/RevengeOS/releases/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        await self.getrevenge(ctx, device)
                    elif fetch.status == 404:
                        device = phone.upper()
                        await self.getrevenge(ctx, device)
                    else:
                        await ctx.send('Cannot reach RevengeOS servers.')
            except Exception as e:
                print('From revenge:')
                print(e)
                return

    @commands.command()
    async def superior(self, ctx, phone):
        device = phone.lower()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://raw.githubusercontent.com/SuperiorOS/official_devices/pie/{device}.json') as fetch:
                    if fetch.status == 404:
                        device = phone.upper()
                        await self.getsuperior(ctx, device)
                    elif fetch.status == 200:
                        await self.getsuperior(ctx, device)
        except Exception as e:
            print('From Superior:')
            print(e)
            return

    @commands.command()
    async def aosip(self, ctx, phone, version='official'):
        device = phone.lower()
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://aosip.dev/{device}/{version}') as fetch:
                if fetch.status == 200:
                    await self.getaosip(ctx, device, version)
                else:
                    device = phone.upper()
                    await self.getaosip(ctx, device, version)


def setup(bot):
    bot.add_cog(ROMResolver(bot))
