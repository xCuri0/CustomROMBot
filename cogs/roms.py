from discord.ext import commands
from requests import get
from hurry.filesize import size
import json

class ROMResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def posp(self, ctx, device):
        fetch = get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly')
        if fetch.status_code == 200 and str(fetch.json()['response']) != "[]":
            usr = fetch.json()
            filesize = size(int(usr['response'][-1]['size']))
            reply_text = f"**Download:** {usr['response'][-1]['filename']}\n" \
                         f"**URL:** {usr['response'][-1]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][-1]['version']}`"
            await ctx.send(reply_text)
        else:
            await ctx.send('Device not found!')

    @commands.command()
    async def posptest(self, ctx, device):
        fetch = get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=mashed')
        if fetch.status_code == 200 and str(fetch.json()['response']) != "[]":
            usr = fetch.json()
            filesize = size(int(usr['response'][-1]['size']))
            reply_text = f"**Download:** {usr['response'][-1]['filename']}\n" \
                         f"**URL:** {usr['response'][-1]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][-1]['version']}`"
            await ctx.send(reply_text)
        else:
            ctx.send('Device not found!')

    @commands.command()
    async def evo(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            filesize = size(int(usr['size']))
            reply_text = f"**Download:** `{usr['filename']}`\n" \
                         f"**URL:** {usr['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Android Version:** `{usr['version']}`\n" \
                         f"**Maintainer:** {usr['maintainer']}: {usr['maintainer_url']}\n" \
                         f"**XDA Thread:** {usr['forum_url']}"
            await ctx.send(reply_text)
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")

    @commands.command()
    async def viper(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/Viper-Devices/official_devices/master/{device}/build.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            filesize = size(int(usr['response'][0]['size']))
            reply_text = f"**Download:** `{usr['response'][0]['filename']}`\n" \
                         f"**URL:** {usr['response'][0]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][0]['version']}`\n"
        elif fetch.status_code == 404:
            reply_text = 'Device not found!'
        await ctx.send(reply_text)

    @commands.command()
    async def dotos(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/DotOS/ota_config/dot-p/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            filesize = size(int(usr['response'][0]['size']))
            reply_text = f"**Download:** `{usr['response'][0]['filename']}`\n" \
                         f"**URL:** {usr['response'][0]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][0]['version']}`\n"
        elif fetch.status_code == 404:
            reply_text = 'Device not found!'
        await ctx.send(reply_text)

    @commands.command()
    async def pearl(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/PearlOS/OTA/master/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            filesize = size(int(usr['response'][0]['size']))
            reply_text = f"**Download:** `{usr['response'][0]['filename']}`\n" \
                         f"**URL:** {usr['response'][0]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][0]['version']}`\n" \
                         f"**XDA Thread:** `{usr['response'][0]['xda']}`"
        elif fetch.status_code == 404:
            reply_text = 'Device not found!'
        await ctx.send(reply_text)

    @commands.command()
    async def pixy(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/PixysOS-Devices/official_devices/master/{device}/build.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            filesize = size(int(usr['response'][0]['size']))
            reply_text = f"**Download:** `{usr['response'][0]['filename']}`\n" \
                         f"**URL:** {usr['response'][0]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][0]['version']}`\n"
        elif fetch.status_code == 404:
            reply_text = 'Device not found!'
        await ctx.send(reply_text)

    @commands.command()
    async def havoc(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/Havoc-Devices/android_vendor_OTA/pie/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            filesize = size(int(usr['response'][0]['size']))
            reply_text = f"**Download:** `{usr['response'][0]['filename']}`\n" \
                         f"**URL:** {usr['response'][0]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][0]['version']}`\n"
        elif fetch.status_code == 404:
            reply_text = 'Device not found!'
        await ctx.send(reply_text)

    @commands.command()
    async def lineage(self, ctx, device):
        fetch = get(f'https://download.lineageos.org/api/v1/{device}/nightly/*')
        if fetch.status_code == 200 and str(fetch.json()['response']) != "[]":
            usr = fetch.json()
            filesize = size(int(usr['response'][-1]['size']))
            reply_text = f"**Download:** {usr['response'][-1]['filename']}\n" \
                         f"**URL:** {usr['response'][-1]['url']}\n" \
                         f"**Size:** `{filesize}`\n" \
                         f"**Version:** `{usr['response'][-1]['version']}`\n" \
                         f"**Type:** {usr['response'][-1]['romtype']}"
            await ctx.send(reply_text)
        else:
            await ctx.send('Device not found!')


def setup(bot):
    bot.add_cog(ROMResolver(bot))
