import os

BOT_TOKEN = os.environ.get('5615528335:AAHOlk2j2TE5CWOv24mxBwpBMAx2ui3Zv1k')
API_ID = 14091414
SESSION_STRING = os.environ.get('SESSION_STRING', '')
API_HASH = os.environ.get('5615528335:AAHOlk2j2TE5CWOv24mxBwpBMAx2ui3Zv1k')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '5500572462').split()))
LOG_GROUP_ID = int(os.environ.get('-1001646246141'))
GBAN_LOG_GROUP_ID = int(os.environ.get('-1001646246141'))
MESSAGE_DUMP_CHAT = int(os.environ.get('-1001646246141'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('mongodb+srv://Zoro:Zoro@cluster0.x1vigdr.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('JEQHPA-MRCARX-SUEPKY-DSXOAP-ARQ')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
