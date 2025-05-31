# simple-online-bot
Gives a discord bot an online presence

Image: nzspongebob/simple-online-bot:latest

A Simple Discord Online Presence Bot

This Docker image runs a lightweight Python-based Discord bot whose primary function is to connect to Discord and maintain an "online" presence. It's designed to be minimal and easy to configure for users who simply need a bot to appear online in their server, optionally displaying a custom status message.

Features:

Connects to Discord using a provided bot token.
Maintains a persistent "online" status.
Allows customization of the bot's activity (e.g., "Playing a game," "Listening to music," "Watching something").
Configurable via environment variables.
Requirements:

A Discord Bot Token from the Discord Developer Portal. https://discord.com/developers/applications
The "Presence Intent" must be enabled for your bot application in the Discord Developer Portal (under Bot -> Privileged Gateway Intents).


Environment Variables:

To configure the bot, use the following environment variables when running the Docker container:

Variable: DISCORD_BOT_TOKEN -
Required: Yes -
Default Value: (none) -
Description: Your Discord bot's authentication token. The bot will not start without this.

Variable: BOT_ACTIVITY_NAME -
Required: No -
Default Value: being online -
Description: The text that appears as the bot's activity (e.g., if the activity type is "playing", this is the game name).

Variable: BOT_ACTIVITY_TYPE -
Required: No -
Default Value: playing -
Description: The type of activity the bot displays. Valid options are: playing, listening, watching, streaming.

Variable: BOT_STREAM_URL -
Required: No -
Default Value: https://www.twitch.tv/... (This is a placeholder) -
Description: This variable is only used if BOT_ACTIVITY_TYPE is set to streaming. It should be the URL for the stream (e.g., a
Twitch or YouTube Live URL). If BOT_ACTIVITY_TYPE is streaming and this URL is not provided or is invalid, the bot's streaming status may not display as intended.


Example Usage (Docker CLI):
Bash

docker run -d \
  --name my-discord-online-bot \
  -e DISCORD_BOT_TOKEN="YOUR_DISCORD_BOT_TOKEN_HERE" \
  -e BOT_ACTIVITY_NAME="with servers" \
  -e BOT_ACTIVITY_TYPE="playing" \
  nzspongebob/simple-online-bot:latest

Example Usage (Docker Compose compose.yml):

YAML

version: '3.8'
services:
  discord_bot:
    image: nzspongebob/simple-online-bot:latest
    container_name: my-discord-online-bot
    restart: unless-stopped
    environment:
      - DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
      - BOT_ACTIVITY_NAME=with servers
      - BOT_ACTIVITY_TYPE=playing
      # - BOT_STREAM_URL=your_stream_url_if_streaming

Notes:

Bot must already be invited to your Discord server(s).
This bot does not include any command handling or message processing features. Its one and only purpose is to maintain an online presence.
