from click import command
from nextcord import InteractionResponse
from nextcord.ext import commands
from config import VERIFIED_DISCORD_ID
from utils.embedder import embed_success
from .role_view import VerifyView


class Verify(commands.Cog, name="Verify"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     """Call when the cog is loaded"""
    #     self.bot.add_view(VerifyView())

    @commands.command()
    # @commands.is_owner()
    async def verify(self, ctx):
        # view = VerifyView()
        
        await ctx.send(f'Welcome to the verification process {ctx.author.name}!', view=VerifyView())
        # await view.wait()
        # print(f"{VERIFIED_DISCORD_ID}")
        # if view.value is None:
        #     return
        # elif view.value:
        #     for VerificationCheck in VERIFIED_DISCORD_ID:
        #         if ctx.author.id == int(VerificationCheck):
                    
        #             await ctx.send(f"{ctx.author.name}'s Verification process Passed!")
        #             # await ctx.add_roles(968136113342545930)
        #             return
        #         else:
        #             await ctx.send(f"{ctx.author.name}'s Verfication process Failed. Please contact our staff members.")
        #             return         
        # else:
        #     return

# This function will be called when this extension is loaded.
# It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
    bot.add_cog(Verify(bot))
