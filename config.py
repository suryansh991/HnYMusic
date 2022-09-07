from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/bd8c1e1c0376d818c13b5.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DarkestMarket666")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/DarkestXMarket666")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1574818111").split()))
