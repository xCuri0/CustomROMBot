from discord.ext import commands
import discord
import aiohttp

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950"


class GAppsResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gapps(self, ctx, arch, version, variant):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.github.com/repos/opengapps/arm64/tags') as tags:
                usr = await tags.json()
                value = f"**Build date**: `{usr[0]['name']}`\n" \
                        f"**Arch**: `{arch}`\n" \
                        f"**Variant**: `{variant}`\n" \
                        f"**Android Version**: `{version}`\n" \
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
