# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


import json
import os


def get_user_list(config, key):
    with open("{}/Mikobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 25475489 # Get this value from my.telegram.org/apps
    API_HASH = "3fc2b371f4fbb0166758736414d8be92"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://avnadmin:AVNS_yeAUK7te1DAZR79yUuj@choco-chocoxgithub-f883.c.aivencloud.com:16510/defaultdb?sslmode=require"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002400130574
    MESSAGE_DUMP = -1002400130574

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Choco:Choco@cluster0.rohac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "https://t.me/ANIME_CHAT_ANG"
    SUPPORT_ID = -1002195515883

    # Database name
    DB_NAME = ""

    # Bot token
    TOKEN = "7764287955:AAE0zQiW7YdZouzfj70pxtWG_zp9FsCHAD0"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 1266240012
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    DEMONS = get_user_list("elevated_users.json", "supports")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True
    BAN_STICKER = (
        "CAACAgUAAxkBAAEGWC5lloYv1tiI3-KPguoH5YX-RveWugACoQ4AAi4b2FQGdUhawbi91DQE"
    )

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
