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


class DeviceNotFoundError(Exception):
    pass


class DeviceChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    reply_text = ''
    check = False
    timeout = aiohttp.ClientTimeout(total=3)

    async def getaexoreo(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(f'https://api.aospextended.com/ota/{device}/pie') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        self.reply_text += 'AEX (Pie)\n'
                    elif usr['error']:
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(f'https://api.aospextended.com/ota/{device.upper}/pie') as fetch:
                    if not usr['error']:
                        self.reply_text += 'AEX (Pie)\n'
            except Exception as e:
                print('From getaaexoreo: ')
                print(e)

    async def getaexpie(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(f'https://api.aospextended.com/ota/{device}/oreo') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        self.reply_text += 'AEX (Oreo)\n'
                    elif usr['error']:
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(f'https://api.aospextended.com/ota/{device.upper()}/oreo') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        self.reply_text += 'AEX (Oreo)\n'
            except Exception as e:
                print('From getaaexpie: ')
                print(e)

    async def getbtlg(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get('https://bootleggersrom-devices.github.io/api/devices.json') as devices:
                    if devices.status == 200:
                        usr = await devices.json()
                        if usr.get(device) is not None:
                            self.reply_text += 'BootleggersROM\n'
                        elif usr.get(device) is None:
                            raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get('https://bootleggersrom-devices.github.io/api/devices.json') as devices:
                    if devices.status == 200:
                        usr = await devices.json()
                        if usr.get(device.upper()) is not None:
                            self.reply_text += 'BootleggersROM\n'
            except Exception as e:
                print('From btlg: ')
                print(e)

    async def getpe(self, device: str):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                    usr = await fetch.json()
                    if not usr['error']:
                        self.reply_text += 'Pixel Experience (Pie)\n'
                    elif usr['error']:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device.upper()}/pie') as fetch:
                    usr = await fetch.json()
                    if not usr['error']:
                        self.reply_text += 'Pixel Experience (Pie)\n'
        except:
            return
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                    usr = await fetch.json()
                    if not usr['error']:
                        self.reply_text += 'Pixel Experience (Pie-CAF)\n'
                    elif usr['error']:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device.upper()}/pie_caf') as fetch:
                    usr = await fetch.json()
                    if not usr['error']:
                        self.reply_text += 'Pixel Experience (Pie-CAF)\n'
        except:
            return
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo') as fetch:
                    usr = await fetch.json()
                    if not usr['error']:
                        self.reply_text += 'Pixel Experience (Oreo)\n'
                    elif usr['error']:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device.upper()}/oreo') as fetch:
                    usr = await fetch.json()
                    if not usr['error']:
                        self.reply_text += 'Pixel Experience (Oreo)\n'
        except Exception as e:
            print('From pe: ')
            print(e)

    async def getlineage(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += 'LineageOS\n'
                    elif str(usr['response']) == '[]':
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(f'https://download.lineageos.org/api/v1/{device.upper()}/nightly/*') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += 'LineageOS\n'
            except Exception as e:
                print('From lineage: ')
                print(e)

    async def gethavoc(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json') as fetch:
                    usr = await fetch.json(content_type=None)
                    if str(usr['response']) != '[]':
                        self.reply_text += 'HavocOS\n'
                    elif str(usr['response']) == '[]':
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(
                        f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device.upper()}.json') as fetch:
                    usr = await fetch.json(content_type=None)
                    if str(usr['response']) != '[]':
                        self.reply_text += 'HavocOS\n'
            except Exception as e:
                print('From havoc: ')
                print(e)

    async def getpixys(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PixysOS\n'
                    elif fetch.status == 404:
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(
                        f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device.upper()}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PixysOS\n'
            except Exception as e:
                print('From pixys: ')
                print(e)

    async def getpearl(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PearlOS\n'
                    elif fetch.status == 404:
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device.upper()}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PearlOS\n'
            except Exception as e:
                print('From pearl: ')
                print(e)

    async def getdot(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'DotOS\n'
            except Exception as e:
                print('From dot: ')
                print(e)

    async def getviper(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'ViperOS\n'
            except Exception as e:
                print('From viper: ')
                print(e)

    async def getevo(self, device: str):
        if device == 'enchilada':
            return
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(
                        f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Evolution-X\n'
                    elif fetch.status == 404:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(
                        f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device.upper()}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Evolution-X\n'
        except Exception as e:
            print('From evo: ')
            print(e)

    async def getpotato(self, device: str):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False), timeout=self.timeout) as session:
            try:
                async with session.get(
                        f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += "Potato Open Sauce Project \n"
                    elif fetch.status != 200 or str(usr['response']) == '[]':
                        raise DeviceNotFoundError
            except aiohttp.ClientConnectionError:
                async with session.get(
                        f'http://api.strangebits.co.in/checkUpdate?device={device}&type=weekly') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += "Potato Open Sauce Project \n"
                    elif fetch.status != 200 or str(usr['response']) == '[]':
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                try:
                    async with session.get(
                            f'https://api.potatoproject.co/checkUpdate?device={device.upper}&type=weekly') as fetch:
                        usr = await fetch.json()
                        if fetch.status == 200 and str(usr['response']) != '[]':
                            self.reply_text += "Potato Open Sauce Project \n"
                except aiohttp.ClientConnectionError:
                    async with session.get(
                            f'http://api.strangebits.co.in/checkUpdate?device={device.upper}&type=weekly') as fetch:
                        usr = await fetch.json()
                        if fetch.status == 200 and str(usr['response']) != '[]':
                            self.reply_text += "Potato Open Sauce Project \n"
            except Exception as e:
                print('From getpotato:')
                print(e)

    async def getcrdroid(self, device: str):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            try:
                async with session.get(
                        'https://raw.githubusercontent.com/crdroidandroid/android_vendor_crDroidOTA/9.0/update.xml') as fetch:
                    fetchawait = await fetch.read()
                    soup = BeautifulSoup(fetchawait.decode('utf-8'), features="lxml")
                    finddevice = soup.find(device)
                    if finddevice is not None:
                        self.reply_text += 'crDroid\n'
                    elif finddevice is None:
                        raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with session.get(
                        'https://raw.githubusercontent.com/crdroidandroid/android_vendor_crDroidOTA/9.0/update.xml') as fetch:
                    fetchawait = await fetch.read()
                    soup = BeautifulSoup(fetchawait.decode('utf-8'), features="lxml")
                    finddevice = soup.find(device.upper())
                    if finddevice is not None:
                        self.reply_text += 'crDroid\n'
            except Exception as e:
                print('From crd: ')
                print(e)

    async def getsyberia(self, device: str):
        if device == 'fajita':
            try:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/OnePlus6T.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)
        elif device == 'enchilada':
            try:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/OnePlus6.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)
        else:
            try:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/a-only/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
                        elif fetch.status == 404:
                            raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(
                            f'https://raw.githubusercontent.com/syberia-project/official_devices/master/a-only/{device.upper()}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)
            try:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
                        elif fetch.status == 404:
                            raise DeviceNotFoundError
            except DeviceNotFoundError:
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/{device.upper()}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
            except Exception as e:
                print('From syb: ')
                print(e)

    async def getrr(self, device: str):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://raw.githubusercontent.com/ResurrectionRemix-Devices/api/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Resurrection Remix \n'
                    elif fetch.status == 404:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://raw.githubusercontent.com/ResurrectionRemix-Devices/api/master/{device.upper()}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Resurrection Remix \n'
        except Exception as e:
            print('From rr: ')
            print(e)

    async def getrevenge(self, device: str):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://raw.githubusercontent.com/RevengeOS/releases/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'RevengeOS\n'
                    elif fetch.status == 404:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://raw.githubusercontent.com/RevengeOS/releases/master/{device.upper()}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'RevengeOS\n'
        except Exception as e:
            print('From getrevenge:')
            print(e)

    async def getsuperior(self, device: str):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://raw.githubusercontent.com/SuperiorOS/official_devices/pie/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'SuperiorOS\n'
                    elif fetch.status == 404:
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'https://raw.githubusercontent.com/SuperiorOS/official_devices/pie/{device.upper()}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'SuperiorOS\n'
        except Exception as e:
            print('From getsuperior')
            print(e)

    async def getaosip(self, device: str):
        try:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'http://aosip.dev/{device}/official') as fetch:
                    usr = await fetch.json(encoding=None)
                    if str(usr['response']) != '[]':
                        self.reply_text += 'AOSiP\n'
                    elif str(usr['response']) == '[]':
                        raise DeviceNotFoundError
        except DeviceNotFoundError:
            async with aiohttp.ClientSession(timeout=self.timeout) as session:
                async with session.get(f'http://aosip.dev/{device.upper()}/official') as fetch:
                    usr = await fetch.json(encoding=None)
                    if str(usr['response']) != '[]':
                        self.reply_text += 'AOSiP\n'
        except Exception as e:
            print('from getaosip')
            print(e)

    async def parallel(self, phone: str):
        self.check = True
        device = phone.lower()
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
            self.getrevenge(device),
            self.getrr(device),
            self.getsuperior(device),
            self.getsyberia(device),
            self.getviper(device),
            self.getaosip(device)
        )

    @commands.command(name="roms")
    async def devicechecker(self, ctx, device=None):
        async with ctx.typing():
            if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.mention_everyone:
                return await ctx.send('NO EVERYONE-ING HERE!')
            if device is None:
                embed = discord.Embed(title="Available ROMs", description=f"{roms}", color=0x5eff72)
                embed.set_footer(text="Bot by Keikei14 | Keikei14#7950")
                await ctx.send(embed=embed)
            else:
                if self.check is True:
                    return
                await self.parallel(device)
                if self.reply_text != '' and self.check is True:
                    embed = discord.Embed(title=f"Available ROMs for {device}",
                                          description=self.reply_text,
                                          color=embedcolor)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                    self.check = False
                else:
                    await ctx.send('No available supported ROMs for device. <:harold:498881491368017930>')
                    self.check = False
                self.reply_text = ''


def setup(bot):
    bot.add_cog(DeviceChecker(bot))
