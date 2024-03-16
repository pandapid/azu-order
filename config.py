#(©)𝔭𝔞𝔫𝔦𝔪𝔢𝔦𝔡




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6387715337:AAG-GouYhc0CHNSFMgP0bifHTWNunCY2Weg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29684228"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9c201a654e8fc97576ce5c077cf529d2")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001954090257"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5531142222"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Eln:Chaik2501@cluster0.9ipuplz.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "pusat")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001871589417"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001694677224"))
FORCE_SUB_GROUP2 = int(os.environ.get("FORCE_SUB_GROUP2", "-1002009423518"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention} 👋, Enjoy disini.\n\n join @bahan_asupan_sma</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "869513589 6707869392").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {mention},\n\n Join dulu ke channel/ grup dibawah untuk ambil file</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

USCH = os.environ.get("USCH", "@bahan_asupan_sma")
USOW = os.environ.get("USOW", "@bahan_asupan_dood")

ADMINS.append(OWNER_ID)
ADMINS.append(1474271232)

LOG_FILE_NAME = "azusa.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
