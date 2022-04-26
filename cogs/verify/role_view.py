from distutils.command.config import config
import nextcord
import config

def custom_id(view: str, id: int) -> str:
    """Return the view with the id"""
    return f"{config.BOT_NAME}:{view}:{id}"

VIEW_NAME = "VerifyView"

class VerifyView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=1*60)
        self.value = None
        
    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        
        role_id = config.VERIFIED_ROLE_ID
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        # if user already has the role
        if role in interaction.user.roles:
            await interaction.response.send_message("You are already verified!",ephemeral=True)
            return
        # if user does not have the role
        else:
            for check_id in config.VERIFIED_DISCORD_ID:
                print(f"{interaction.user.id} {int(check_id)}")
                if interaction.user.id == int(check_id):
                    await interaction.user.add_roles(role)
                    await interaction.response.send_message("You are successfully verified!",ephemeral=True)
                    return
                else:
                    await interaction.response.send_message("Verification failed. Please contact staff members if this is a problem.",ephemeral=True)
                    return
        
    @nextcord.ui.button(label="Verify", emoji="✅", style=nextcord.ButtonStyle.green, custom_id=custom_id(VIEW_NAME, config.VERIFIED_ROLE_ID))
    async def verify(self, button, interaction):
        await self.handle_click(button, interaction)
        
    @nextcord.ui.button(label="Cancel", emoji="⛔", style=nextcord.ButtonStyle.red)
    async def cancel(self, button, interaction):
        await interaction.response.send_message("Verification cancelled.",ephemeral=True)