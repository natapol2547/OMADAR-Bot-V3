import os

from dotenv.main import load_dotenv

load_dotenv()


BOT_NAME = "OMADAR"

# Discord config
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
BOT_PREFIX = "omadar! "

VERIFIED_DISCORD_ID = os.getenv("VERIFIED_DISCORD_ID", "").split(',')

ARTIST_ROLE_ID=int(os.getenv("ARTIST_ROLE_ID", ""))
COLLECTOR_ROLE_ID=int(os.getenv("COLLECTOR_ROLE_ID", ""))
TOKEN_STAKER_ROLE_ID=int(os.getenv("TOKEN_STAKER_ROLE_ID",  ""))
OTHER_ROLE_ID=int(os.getenv("OTHER_ROLE_ID", ""))

VERIFIED_ROLE_ID=int(os.getenv("VERIFIED_ROLE_ID", ""))
UNVERIFIED_ROLE_ID=int(os.getenv("UNVERIFIED_ROLE_ID", ""))

# Channel IDs
VERIFICATION_CHANNEL_ID=int(os.getenv("VERIFICATION_CHANNEL_ID", ""))
TESTING_CHANNEL_ID=int(os.getenv("TESTING_CHANNEL_ID", ""))