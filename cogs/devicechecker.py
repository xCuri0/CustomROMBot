from discord.ext import commands
import discord
import aiohttp
from bs4 import BeautifulSoup

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950"
roms = 'DotOS (dotos)\n' \
       'Evolution-X (evo)\n' \
       'HavocOS (havoc)\n' \
       'PearlOS (pearl)\n' \
       'PixysOS (pixy)\n' \
       'Potato Open Sauce Project (posp)\n' \
       'ViperOS (viper)\n' \
       'LineageOS (los/lineage)\n' \
       'Pixel Experience (pe) \n' \
       'BootleggersROM (btlg/bootleggers) \n' \
       'AOSP Extended (aex) \n' \
       'crDroid (crdroid)\n' \
       'Syberia (syberia)\n' \
       'Resurrection Remix (rr)\n'


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
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From getaaexoreo: ')
                print(e)
                pass

    async def getaexpie(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://api.aospextended.com/ota/{device}/oreo') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        self.reply_text += 'AEX (Oreo)\n'
                    else:
                        pass
                    await session.close()
            except Exception as e:
                print('From getaaexpie: ')
                print(e)
                pass

    async def getbtlg(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('https://bootleggersrom-devices.github.io/api/devices.json') as devices:
                    if devices.status == 200:
                        usr = await devices.json()
                        if device in usr:
                            self.reply_text += 'BootleggersROM\n'
                        else:
                            pass
                    else:
                        pass
                    await session.close()
            except Exception as e:
                print('From btlg: ')
                print(e)
                pass

    async def getpe(self, device):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                        usr = await fetch.json()
                        if not usr['error']:
                            self.reply_text += 'Pixel Experience (Pie)\n'
                        else:
                            pass
                        await session.close()
            except:
                pass
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                        usr = await fetch.json()
                        if not usr['error']:
                            self.reply_text += 'Pixel Experience (Pie-CAF)\n'
                        await session.close()
            except:
                pass
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo') as fetch:
                        usr = await fetch.json()
                        if not usr['error']:
                            self.reply_text += 'Pixel Experience (Oreo)\n'
                        await session.close()
            except Exception as e:
                print('From pe: ')
                print(e)
                pass

    async def getlineage(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += 'LineageOS\n'
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From lineage: ')
                print(e)
                pass

    async def gethavoc(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json') as fetch:
                    if fetch.status == 200:
                        usr = await fetch.json(content_type=None)
                        if str(usr['response']) != '[]':
                            self.reply_text += 'HavocOS\n'
                        else:
                            pass
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From havoc: ')
                print(e)
                pass

    async def getpixys(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PixysOS\n'
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From pixys: ')
                print(e)
                pass

    async def getpearl(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'PearlOS\n'
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From pearl: ')
                print(e)
                pass

    async def getdot(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'DotOS\n'
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From dot: ')
                print(e)
                pass

    async def getviper(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'ViperOS\n'
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From viper: ')
                print(e)
                pass

    async def getevo(self, ctx, device):
        if device == 'enchilada':
            ctx.send('No available supported ROMs for device. <:harold:498881491368017930>')
        elif device != 'enchilada':
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                            f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Evolution-X\n'
                        else:
                            pass
                    await session.close()
            except Exception as e:
                print('From evo: ')
                print(e)
                pass

    async def getpotato(self, device):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        self.reply_text += "Potato Open Sauce Project \n"
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From potat: ')
                print(e)
                pass

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
                    else:
                        pass
                await session.close()
            except Exception as e:
                print('From crd: ')
                print(e)
                pass

    async def getsyberia(self, device):
        if device == 'fajita':
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/OnePlus6T.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
                        else:
                            pass
                await session.close()
            except Exception as e:
                print('From syb: ')
                print(e)
                pass
        elif device == 'enchilada':
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/OnePlus6.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
                        else:
                            pass
                await session.close()
            except Exception as e:
                print('From syb: ')
                print(e)
                pass
        elif device != 'fajita' or device != 'enchilada':
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/a-only/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
                        else:
                            pass
                await session.close()
            except Exception as e:
                print('From syb: ')
                print(e)
                pass
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/{device}.json') as fetch:
                        if fetch.status == 200:
                            self.reply_text += 'Syberia\n'
                        else:
                            pass
                await session.close()
            except Exception as e:
                print('From syb: ')
                print(e)
                pass
        else:
            pass

    async def getrr(self, device):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://raw.githubusercontent.com/ResurrectionRemix-Devices/api/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        self.reply_text += 'Resurrection Remix \n'
                    else:
                        pass
            await session.close()
        except Exception as e:
            print('From rr: ')
            print(e)
            pass

    @commands.command(name="roms")
    async def devicechecker(self, ctx, device=None):
        if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.mention_everyone:
            return await ctx.send('NO EVERYONE-ING HERE!')
        if device is None:
            embed = discord.Embed(title="Available ROMs", description=f"{roms}", color=0x5eff72)
            embed.set_footer(text="Bot by Keikei14 | Keikei14#7950")
            await ctx.send(embed=embed)
        elif device is not None:
            await self.getrr(device)
            await self.getaexoreo(device)
            await self.getaexpie(device)
            await self.getbtlg(device)
            await self.getpe(device)
            await self.getlineage(device)
            await self.gethavoc(device)
            await self.getpearl(device)
            await self.getpixys(device)
            await self.getdot(device)
            await self.getviper(device)
            await self.getevo(ctx, device)
            await self.getpotato(device)
            await self.getcrdroid(device)
            await self.getsyberia(device)
            if self.reply_text != '':
                embed = discord.Embed(title=f"Available ROMs for {device}",
                                      description=self.reply_text,
                                      color=embedcolor)
                embed.set_footer(text=embedfooter)
                await ctx.send(embed=embed)
            elif self.reply_text == '':
                await ctx.send('No available supported ROMs for device. <:harold:498881491368017930>')


def setup(bot):
    bot.add_cog(DeviceChecker(bot))
