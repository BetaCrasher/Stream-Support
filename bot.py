import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Bot is online')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.channel) == 'general' and 'twitch.tv/' in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send('Pls post links in their respective advertise channels. Thank you')

    if message.content.startswith('$purge') and str(message.author) == 'BetaCrasher#6993':
        await message.channel.purge()

client.run('NzEyMDQ0MDY4MDU3OTA3MjYx.XsL0zQ.dlE3ftN604JziBIEo2Ijy3Ucsns')
