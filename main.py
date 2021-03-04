import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?cantjoin'):
        await message.channel.send('Follow these steps to fix most of the common problems when joining!\n\n\t **Step 1:** Ensure you are on Java 1.16.4/5. You can join from either 1.16.4 or .5\n\n\t **Step 2:** Restart your game and launcher.\n\n\t **Step 3:** Are you joining from the Java version of Minecraft? You cannot join jonahwill.org from bedrock or Pocket Edition.\n\n If these steps have not worked, open a ticket and we will get back to you asap.')

    if message.content.startswith('?ip'):
        await message.channel.send('To join the server use this IP:\n`jonahwill.org`')

keep_alive()
client.run(os.getenv('TOKEN'))