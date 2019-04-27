from discord.ext import commands
from requests import get
from hurry.filesize import size
import discord
from datetime import date

embedcolor = 0x5eff72
embedfooter = "bot was made by Keikei14 | Keikei14#7950"


class ROMResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def posp(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly')
        if fetch.status_code == 200 and str(fetch.json()['response']) != "[]":
            usr = fetch.json()
            builddate = date.fromtimestamp(usr['response'][-1]['datetime'])
            filesize = size(int(usr['response'][-1]['size']))
            valued = f"[{usr['response'][-1]['filename']}]({usr['response'][-1]['url']})\n" \
                     f"Build Date: {builddate}\n" \
                     f"Build Size: {filesize}\n" \
                     f"Version: {usr['response'][-1]['version']}"
            embed = discord.Embed(title="Potato Open Source Project Latest Build:",
                                  description=valued,
                                  color=embedcolor)
            embed.set_footer(text=embedfooter)
            await ctx.send(embed=embed)
        else:
            await ctx.send('Device not found!')

    @commands.command()
    async def evo(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
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
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def viper(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json')
        if fetch.status_code == 200:
            usr = fetch.json()
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
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def dotos(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
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
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def pearl(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
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
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def pixy(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json')
        if fetch.status_code == 200:
            usr = fetch.json()
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
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def havoc(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
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
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def lineage(self, ctx, phone):
        device = phone.lower()
        fetch = get(f'https://download.lineageos.org/api/v1/{device}/nightly/*')
        if fetch.status_code == 200 and str(fetch.json()['response']) != "[]":
            usr = fetch.json()
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

    @commands.command()
    async def pe(self, ctx, phone, peversion=None):
        device = phone.lower()
        if peversion is None:
            fetch = get(f'https://download.pixelexperience.org/ota_v2/{device}/pie')
        elif peversion.lower() == 'caf':
            fetch = get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf')
        elif peversion.lower() == 'pie_caf':
            fetch = get(f'https://download.pixelexperience.org/ota_v2/{device}/pie_caf')
        elif peversion.lower() == 'oreo':
            fetch = get(f'https://download.pixelexperience.org/ota_v2/{device}/oreo')
        else:
            return await ctx.send('Device/Version not found!')
        usr = fetch.json()
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
