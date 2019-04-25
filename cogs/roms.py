from discord.ext import commands
from requests import get


class ROMResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def posp(self, ctx, device):
        fetch = get(f'https://api.potatoproject.co/checkUpdate?device={device}&type=weekly')
        if fetch.status_code == 200 and str(fetch.json()['response']) != "[]":
            usr = fetch.json()
            reply_text = f"*Download:* [{usr['response'][-1]['filename']}]\n" \
                         f"*URL:* {usr['response'][-1]['url']}\n" \
                         f"*Size:* `{usr['response'][-1]['size']}`\n" \
                         f"*Version:* `{usr['response'][-1]['version']}`"
        await ctx.send(reply_text)

    @commands.command()
    async def evo(self, ctx, device):
        fetch = get(f'https://raw.githubusercontent.com/evolution-x/official_devices/master/builds/{device}.json')
        if fetch.status_code == 200:
            usr = fetch.json()
            reply_text = f"*Download:* `{usr['filename']}`\n" \
                         f"*URL:* {usr['url']}\n" \
                         f"*Size:* `{usr['size']}`\n" \
                         f"*Android Version:* `{usr['version']}`\n" \
                         f"*Maintainer:* {usr['maintainer']}: {usr['maintainer_url']}\n" \
                         f"*XDA Thread:* {usr['forum_url']}"
            await ctx.send(reply_text)
        elif fetch.status_code == 404:
            await ctx.send("Device not found!")


def setup(bot):
    bot.add_cog(ROMResolver(bot))
