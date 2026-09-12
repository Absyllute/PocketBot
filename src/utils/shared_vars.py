# This file is used to store commonly used global / shared variables
# "wah wah wah, this isnt best practice" - kindly stfu as your opinion was not needed :heart: ~Absyllute

from discord import Interaction, Member, app_commands
### --- Utils --- ###
smp_link = "play.pocketcraft-smp.online"

class Config:
    mod_roles: set[int] = set() # "Hello everyone, this is your daily dose of type safety" ~Probably vit12

    @staticmethod
    def is_mod_or_admin():
        def predicate(interaction: Interaction) -> bool:
            if not isinstance (interaction.user, Member):
                return False

            if interaction.user.guild_permissions.administrator:
                return True

            user_roles = [role.id for role in interaction.user.roles]

            for role_id in user_roles:
                if role_id in Config.mod_roles:
                    return True

            return False
        return app_commands.check(predicate=predicate)

### --- Styling --- ###
primary_colour = 0x73d01e
error_colour   = 0xf03c2e