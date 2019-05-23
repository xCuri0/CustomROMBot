from discord.ext import commands
import discord
import aiohttp
from hurry.filesize import size

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950"


class GAppsResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gapps(self, ctx, architecture: str, androidversion: str, gappsvariant: str):
        arch = architecture.lower()
        version = androidversion.lower()
        variant = gappsvariant.lower()
        if arch == 'arm64' and version == '4.4':
            return await ctx.send("ARM64 not available for 4.4")
        elif arch == 'x86' and variant == "aroma" or arch == 'x86_64' and variant == 'aroma':
            return await ctx.send("Aroma variant not available for x86 or x86_64")
        elif arch == 'x86_64' and version == "4.4":
            return await ctx.send("x86_64 not available for 4.4")
        else:
            pass
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.github.com/repos/opengapps/arm64/tags') as tags:
                usr = await tags.json()
            async with session.get(f"https://github.com/opengapps/{arch}/releases/download/{usr[0]['name']}/open_gapps-{arch}-{version}-{variant}-{usr[0]['name']}.zip") as file:
                headers = file.headers
                filesize = size(int(headers['Content-Length']))
                value = f"**Build date**: `{usr[0]['name']}`\n" \
                        f"**Size**: `{filesize}`\n" \
                        f"**Download link:** [open_gapps-{arch}-{version}-{variant}-{usr[0]['name']}](" \
                        f"https://github.com/opengapps/{arch}/releases/download/{usr[0]['name']}/open_gapps-{arch}-{version}-{variant}-{usr[0]['name']}.zip)"
                if tags.status == 200:
                    embed = discord.Embed(title='OpenGAPPS', color=embedcolor, description=value)
                    embed.set_footer(text=embedfooter)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Cannot reach OpenGAPPS servers")

    @gapps.error
    async def gapps_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing parameters. Please do !gapps (arch) (android version) (gapps variant)')
            return


def setup(bot):
    bot.add_cog(GAppsResolver(bot))
