# (c) @AbirHasan2005

import os

class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("11222461"))
    API_HASH = os.environ.get("58de056b4c450ec866592b446d5acfee")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("BQBEjq4HbfVFHQUBxE_msv7k_lZo9CzRpFSvZifW6vKmBuSCB52mqAwot8j0eEyC0nx8tkCXbYFzDE_df_1dK3l8ZLQIOteAefHXt775rqS0NxU_R1ni6srYm58E0afsaC6-JWMlVUEhz2Fu6yBk8Bxie29AmzGM9W-_4Qg3mGJnxA9yLG6R1rEcOz52ZXE21NZ6qE3yRxD-yWnryVlHaTmwGdPQxXjxGT9AYG8Wxc5IWSdldfZ_-GL-jnuQkSCPf6TRk64G7b6VQ5K_IRafau9MtebSBeYZ4PMfsNA4oJVALkgrWhhsa0p6IeNNoBp4UYagXWAPpmF9hu49X2PYBAwKIxf5EgA")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-1001477831252").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-1001646213934").split()))
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
