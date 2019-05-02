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
       'Syberia (syberia)\n'


class DeviceChecker(commands.Cog):

    @commands.command(name="roms")
    async def devicechecker(self, ctx, device=None):
        if "@everyone" in ctx.message.content or "@here" in ctx.message.content or ctx.message.mention_everyone:
            return await ctx.send('NO EVERYONE-ING HERE!')
        reply_text = ''
        if device is None:
            embed = discord.Embed(title="Available ROMs", description=f"{roms}", color=0x5eff72)
            embed.set_footer(text="Bot by Keikei14 | Keikei14#7950")
            await ctx.send(embed=embed)
        elif device is not None:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.aospextended.com/ota/{device}/pie') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        reply_text += 'AEX (Pie)\n'
                    else:
                        pass
                async with session.get(f'https://api.aospextended.com/ota/{device}/oreo') as fetch:
                    usr = await fetch.json(content_type=None)
                    if not usr['error']:
                        reply_text += 'AEX (Oreo)\n'
                    else:
                        pass
                async with session.get('https://bootleggersrom-devices.github.io/api/devices.json') as devices:
                    if devices.status == 200:
                        usr = await devices.json()
                        if device in usr:
                            reply_text += 'BootleggersROM\n'
                        else:
                            pass
                    else:
                        pass
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and not usr['error']:
                        reply_text += 'Pixel Experience (Pie)\n'
                    else:
                        pass
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and not usr['error']:
                        reply_text += 'Pixel Experience (Pie-CAF)\n'
                    else:
                        pass
                async with session.get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and not usr['error']:
                        reply_text += 'Pixel Experience (Oreo)\n'
                    else:
                        pass
                async with session.get(f'https://download.lineageos.org/api/v1/{device}/nightly/*') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        reply_text += 'LineageOS\n'
                    else:
                        pass
                async with session.get(
                        f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json') as fetch:
                    if fetch.status == 200:
                        usr = await fetch.json(content_type=None)
                        if str(usr['response']) != '[]':
                            reply_text += 'HavocOS\n'
                        else:
                            pass
                    else:
                        pass
                async with session.get(
                        f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'PixysOS\n'
                    else:
                        pass
                async with session.get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'PearlOS\n'
                    else:
                        pass
                async with session.get(
                        f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'DotOS\n'
                    else:
                        pass
                async with session.get(
                        f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'ViperOS\n'
                    else:
                        pass
                async with session.get(
                        f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'Evolution-X\n'
                    else:
                        pass
                async with session.get(
                        f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly') as fetch:
                    usr = await fetch.json()
                    if fetch.status == 200 and str(usr['response']) != '[]':
                        reply_text += "Potato Open Sauce Project \n"
                    else:
                        pass
                async with session.get(
                        'https://raw.githubusercontent.com/crdroidandroid/android_vendor_crDroidOTA/9.0/update.xml') as fetch:
                    fetchawait = await fetch.read()
                    soup = BeautifulSoup(fetchawait.decode('utf-8'), features="lxml")
                    finddevice = soup.find(device)
                    if finddevice is not None:
                        reply_text += 'crDroid\n'
                    else:
                        pass
                async with session.get(
                    f'https://raw.githubusercontent.com/syberia-project/official_devices/master/a-only/{device}.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'Syberia\n'
                    else:
                        pass
                async with session.get(
                    f'https://raw.githubusercontent.com/syberia-project/official_devices/master/ab/{device}.json') as fetch:
                    if fetch.status == 200:
                        reply_text += 'Syberia\n'
                    else:
                        pass
            if reply_text != '':
                embed = discord.Embed(title=f"Available ROMs for {device}",
                                      description=reply_text,
                                      color=embedcolor)
                embed.set_footer(text=embedfooter)
                await ctx.send(embed=embed)
            elif reply_text == '':
                await ctx.send('No available supported ROMs for device. <:harold:498881491368017930>')


def setup(bot):
    bot.add_cog(DeviceChecker(bot))
