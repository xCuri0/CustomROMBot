from discord.ext import commands
import discord
import aiohttp

embedcolor = 0x5eff72
embedfooter = "Bot by Keikei14 | Keikei14#7950 and IcyMiguel420 | icymiguel420#3599"


class MagiskResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def magisk(self, ctx, version='stable'):
        async with aiohttp.ClientSession() as session:
            if version == 'stable' or version == 'beta':
                async with session.get(f'https://raw.githubusercontent.com/topjohnwu/magisk_files/master/{version}.json') as fetch:
                    usr = await fetch.json(content_type=None)
            elif version == 'canary':
                async with session.get(f'https://raw.githubusercontent.com/topjohnwu/magisk_files/master/canary_builds/canary.json') as fetch:
                    usr = await fetch.json(content_type=None)
            elif version != 'stable' and version != 'beta' and version != 'canary':
                return await ctx.send("I don't recognize that Magisk version. <:harold:498881491368017930>")
            if fetch.status == 200:
                if version == 'stable':
                    embed = discord.Embed(title='Magisk Stable', color=embedcolor)
                elif version == 'beta':
                    embed = discord.Embed(title='Magisk Beta', color=embedcolor)
                elif version == 'canary':
                    embed = discord.Embed(title='Magisk Canary', color=embedcolor)
                embed.add_field(name=f"Magisk", value=f"Version: Magisk v{usr['magisk']['version']} `{usr['magisk']['versionCode']}` \n"
                                                      f"[Download Here!]({usr['magisk']['link']})\n", inline=False)
                embed.add_field(name=f"Magisk Manager", value=f"Version: {usr['app']['version']} `{usr['app']['versionCode']}` \n"
                                                              f"[Download Here!]({usr['app']['link']})\n", inline=False)
                embed.add_field(name=f"Magisk Uninstaller", value=f"[Download Here!]({usr['uninstaller']['link']})\n", inline=False)
                embed.set_footer(text=embedfooter)
                await ctx.send(embed=embed)
            else:
                await ctx.send('Cannot reach Magisk servers. <:harold:498881491368017930>')


def setup(bot):
    bot.add_cog(MagiskResolver(bot))