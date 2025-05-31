# bot.py
import discord
import os
import asyncio

# --- Configuration ---
# The bot token will be read from an environment variable for security.
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
BOT_ACTIVITY_NAME = os.getenv('BOT_ACTIVITY_NAME', "being online") # Default activity if not set
BOT_ACTIVITY_TYPE_STR = os.getenv('BOT_ACTIVITY_TYPE', "playing").lower() # Default to 'playing'

# --- Bot Setup ---
# Enable Presence Intent in your Discord Developer Portal for the bot.
intents = discord.Intents.default()
intents.presences = True

client = discord.Client(intents=intents)

# --- Event: Bot Ready ---
@client.event
async def on_ready():
    """Called when the bot is successfully connected and ready."""
    print(f'Successfully logged in as: {client.user.name} ({client.user.id})')
    print(f'Discord.py version: {discord.__version__}')
    print('Bot is now online and will attempt to maintain presence.')

    # Set the bot's activity (e.g., "Playing being online")
    activity_type = discord.ActivityType.playing # Default
    if BOT_ACTIVITY_TYPE_STR == "listening":
        activity_type = discord.ActivityType.listening
    elif BOT_ACTIVITY_TYPE_STR == "watching":
        activity_type = discord.ActivityType.watching
    elif BOT_ACTIVITY_TYPE_STR == "streaming":
        # For streaming, a URL is typically required, but we'll keep it simple.
        # If you want actual streaming status, you'll need a stream_url.
        activity_type = discord.ActivityType.streaming
        # For a simple "Streaming X" without a real stream, you might need to adjust
        # or it might default to "Playing" if the URL is missing.
        # For simplicity, we'll stick to a name. A proper streaming status needs a URL.
        # If you set type to streaming, provide BOT_STREAM_URL env var.
        stream_url = os.getenv('BOT_STREAM_URL', "https://www.twitch.tv/yourchannel") # Placeholder
        activity = discord.Streaming(name=BOT_ACTIVITY_NAME, url=stream_url)
    else: # Default to playing
        activity = discord.Game(name=BOT_ACTIVITY_NAME)

    if BOT_ACTIVITY_TYPE_STR != "streaming": # Avoid re-creating if already Streaming
        activity = discord.Activity(name=BOT_ACTIVITY_NAME, type=activity_type)

    try:
        await client.change_presence(status=discord.Status.online, activity=activity)
        print(f"Bot presence set to: {BOT_ACTIVITY_TYPE_STR} {BOT_ACTIVITY_NAME}")
    except Exception as e:
        print(f"Error setting presence: {e}")

# --- Main Execution ---
async def main():
    if not BOT_TOKEN:
        print("CRITICAL ERROR: The 'DISCORD_BOT_TOKEN' environment variable is not set.")
        print("The bot cannot start without the token.")
        return

    print("Attempting to connect to Discord...")
    try:
        await client.start(BOT_TOKEN)
    except discord.LoginFailure:
        print("CRITICAL ERROR: Login to Discord failed. Please check the following:")
        print("1. The 'DISCORD_BOT_TOKEN' is correct and valid.")
        print("2. The bot has been added to the intended server(s).")
        print("3. Your internet connection is stable.")
    except discord.PrivilegedIntentsRequired:
        print("CRITICAL ERROR: Privileged Intents (likely Presence Intent) are required but not enabled.")
        print("Please go to your bot's application page on the Discord Developer Portal:")
        print("  -> Bot -> Privileged Gateway Intents -> Enable 'Presence Intent'.")
    except Exception as e:
        print(f"An unexpected error occurred during bot startup or runtime: {e}")
    finally:
        if not client.is_closed():
            print("Closing the connection to Discord.")
            await client.close()
        print("Bot has shut down.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot shutdown requested via KeyboardInterrupt.")
    except Exception as e:
        print(f"An unhandled exception occurred at the top level: {e}")