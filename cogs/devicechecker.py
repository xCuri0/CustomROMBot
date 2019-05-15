from discord.ext import commands
import discord
import aiohttp
import asyncio
from bs4 import BeautifulSoup

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950"
roms = 'AOSP Extended (aex) \n' \
       'Android Open Source illusion Project (aosip)\n' \
       'BootleggersROM (btlg/bootleggers) \n' \
       'crDroid (crdroid)\n' \
       'DotOS (dotos)\n' \
       'Evolution-X (evo)\n' \
       'HavocOS (havoc)\n' \
       'LineageOS (los/lineage)\n' \
       'PearlOS (pearl)\n' \
       'Pixel Experience (pe) \n' \
       'PixysOS (pixy)\n' \
       'Potato Open Sauce Project (posp)\n' \
       'Resurrection Remix (rr)\n' \
       'RevengeOS(revenge)\n' \
       'SuperiorOS(superior)\n' \
       'Syberia (syberia)\n' \
       'ViperOS (viper)\n'


class DeviceChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    reply_text = ''

    async def getaexoreo(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://api.aospextended.com/ota/{device}/pie') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        self.reply_text += 'AEX (Pie)\n'
            except Exception as e:
                print('From getaaexoreo: ')
                print(e)

    async def getaexpie(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://api.aospextended.com/ota/{device}/oreo') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        self.reply_text += 'AEX (Oreo)\n'
            except Exception as e:
                print('From getaaexpie: ')
                print(e)

    async def getbtlg(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('https://bootleggersrom-devices.github.io/api/devices.json') as devices:
                    if devices.status == 200:
                        usr = await devices.json()
                        if usr.get(device) is not None:
                            self.reply_text += 'BootleggersROM\n'
            except Exception as e:
                print('From btlg: ')
                print(e)

    async def getpe(self, device):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                        usr = await fetch.json()
                        if not usr['error']:
                            self.reply_text += 'Pixel Experience (Pie)\n'
            except:
                return
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                        usr = await fetch.json()
                        if not usr['error']:
                            self.reply_text += 'Pixel Experience (Pie-CAF)\n'
            except:
                return
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo') as fetch:
                        usr = await fetch.json()
                        if not usr['error']:
                            self.reply_text += 'Pixel Experience (Oreo)\n'
            except Exception as e:
                print('From pe: ')
                print(e)

    async def getlineage(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += 'LineageOS\n'
            except Exception as e:
                print('From lineage: ')
                print(e)

    async def gethavoc(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json') as fetch:
                    if fetch.status == 200:
                        usr = await fetch.json(content_type=None)
                        if str(usr['response']) != '[]':
                            self.reply_text += 'HavocOS\n'
            except Exception as e:
                print('From havoc: ')
                print(e)

    async def getpixys(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PixysOS\n'
            except Exception as e:
                print('From pixys: ')
                print(e)

    async def getpearl(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PearlOS\n'
            except Exception as e:
                print('From pearl: ')
                print(e)

    async def getdot(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'DotOS\n'
            except Exception as e:
                print('From dot: ')
                print(e)

    async def getviper(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'ViperOS\n'
            except Exception as e:
                print('From viper: ')
                print(e)

    async def getevo(self, device):
        if device == 'enchilada':
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Evolution-X\n'
        except Exception as e:
            print('From evo: ')
            print(e)

    async def getpotato(self, device):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            try:
                async with session.get(
                        f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly') as fetch:
                    usr = await fetch.json()
            except aiohttp.ClientConnectionError:
                async with session.get(
                        f'http://api.strangebits.co.in/checkUpdate?device={device}&type=weekly') as fetch:
                    usr = await fetch.json()
            except Exception as e:
                print('From getpotato:')
                print(e)
            if fetch.status == 200 and str(usr['response']) != '[]':
                self.reply_text += "Potato Open Sauce Project \n"

    async def getcrdroid(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        'https://raw.githubusercontent.com/crdroidandroid/android_vendor_crDroidOTA/9.0/update.xml') as fetch:
                    fetchawait = await fetch.read()
                    soup = BeautifulSoup(fetchawait.decode('utf-8'), features="lxml")
                    finddevice = soup.find(device)
                    if finddevice is not None:
                        self.reply_text += 'crDroid\n'
            except Exception as e:
                print('From crd: ')
                print(e)

    async def getsyberia(self, device):
        if device == 'fajita':
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/OnePlus6T.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)
        elif device == 'enchilada':
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/OnePlus6.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)
        else:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/a-only/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)

    async def getrr(self, device):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://raw.githubusercontent.com/ResurrectionRemix-Devices/api/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Resurrection Remix \n'
        except Exception as e:
            print('From rr: ')
            print(e)

    async def getrevenge(self, device):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://raw.githubusercontent.com/RevengeOS/releases/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'RevengeOS\n'
        except Exception as e:
            print('From getrevenge:')
            print(e)

    async def getsuperior(self, device):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://raw.githubusercontent.com/SuperiorOS/official_devices/pie/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'SuperiorOS\n'
        except Exception as e:
            print('From getsuperior')
            print(e)

    async def getaosip(self, device):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://aosip.dev/{device}/official') as fetch:
                    usr = await fetch.json()
                    if str(usr['response']) != '[]':
                        self.reply_text += 'AOSiP\n'
        except Exception as e:
            print('from getaosip')
            print(e)

    async def parallel(self, device):
        await asyncio.gather(
            self.getaexoreo(device),
            self.getaexpie(device),
            self.getbtlg(device),
            self.getcrdroid(device),
            self.getdot(device),
            self.getevo(device),
            self.gethavoc(device),
            self.getlineage(device),
            self.getpe(device),
            self.getpearl(device),
            self.getpixys(device),
            self.getpotato(device),
            self.getrevenge(device),
            self.getrr(device),
            self.getsuperior(device),
            self.getsyberia(device),
            self.getviper(device),
            self.getaosip(device)
        )

    @commands.command(name="roms")
    async def devicechecker(self, ctx, device=None):
        if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.mention_everyone:
            return await ctx.send('NO EVERYONE-ING HERE!')
        if device is None:
            embed = discord.Embed(title="Available ROMs", description=f"{roms}", color=0x5eff72)
            embed.set_footer(text="Bot by Keikei14 | Keikei14#7950")
            await ctx.send(embed=embed)
        else:
            await self.parallel(device)
            if self.reply_text != '':
                embed = discord.Embed(title=f"Available ROMs for {device}",
                                      description=self.reply_text,
                                      color=embedcolor)
                embed.set_footer(text=embedfooter)
                await ctx.send(embed=embed)
            else:
                await ctx.send('No available supported ROMs for device. <:harold:498881491368017930>')
            self.reply_text = ''


def setup(bot):
    bot.add_cog(DeviceChecker(bot))
