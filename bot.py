import discord
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User

client = commands.Bot(command_prefix='.')


# On start commands go here
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Doing Bot things'))
    print('Bot is online. :)')


# Removes twitch links from general chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.channel) == 'general' and 'twitch.tv/' in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send('Pls post links in their respective advertise channels. Thank you')

    await client.process_commands(message)


# Command to DM all the users on the server
@client.command()
async def dm_all(ctx, *, args=None):
    if args is not None:
        # print(ctx.author+'pinged everyone: "'+args+'"')
        if ctx.author.guild_permissions.administrator:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(args)
                except:
                    print('Could not DM ' + str(member.name))
        else:
            await ctx.send('You are not allowed to use this command')
    else:
        await ctx.send('no args provided')
    await ctx.channel.purge(limit=1)


# Command to DM a spesific user on the server
@client.command()
async def dm(ctx, users: Greedy[User], *, mess=None):
    if users is not None and mess is not None:
        if ctx.author.guild_permissions.administrator:
            for user in users:
                await user.send(mess)
        else:
            await ctx.send('You are not allowed to use this command')
    await ctx.channel.purge(limit=1)


# Test command
@client.command()
async def ping(ctx):
    await ctx.send('pong')


# Deletes all the messages in the channel
@client.command()
async def purge(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge()
    else:
        await ctx.send('You can\'t use this command')

client.run('Your Token Here')
