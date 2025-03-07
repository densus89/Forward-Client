# (c) @AbirHasan2005

import os

class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get(""))
    API_HASH = os.environ.get("")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
