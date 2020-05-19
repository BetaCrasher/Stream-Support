import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')


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

@client.event
async def dm_all(ctx, *, messege=None):
    if messege != None:
        members = ctx.guild.members
        for member in members:
            try:
                await members.send(messege)
            except:
                print('couldnt DM'+member.name)

    
client.run('NzEyMDQ0MDY4MDU3OTA3MjYx.XsL0zQ.dlE3ftN604JziBIEo2Ijy3Ucsns')
