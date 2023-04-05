import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(2992000)
    API_HASH = "235b12e862d71234ea222082052822fd"
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = "BAAtp4AAiklFZt9d80U3D94aovamYcsPffgtIlkqQCrRzgQM4MBPmY9PTAWkIo664WKNh-ZNK9JszAzTsNawcb90T6ltijobQmP5VaCNVFywcE5193-xuQzaOqndjc0I1IhBG38d49wPyodbfMDJ-uJSDuUtA078dp9e3rL2bIuoUYp2LoNpINCH4CiiR1XVSwg4ALLE5nH7nDRTPVOKUarUBnhOT679B4HdY_QrlvwDNlLFK0Z5rh6KAtWEF4oL2N9cqYVIKcWnNrL2Ses0_2DTf2kapaQzwLsaL8nTaco-FJM4SucKXxChn4UVsSpeRYlvcf7J8DatG7cspsazb-qywzvX1QAAAAFsXZNOAA"
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = []
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = []
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(3)
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
