import discord
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User

client = commands.Bot(command_prefix='.')



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Doing Bot things'))
    print('Bot is online. :)')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.channel) == 'general' and 'twitch.tv/' in message.content:
        await message.channel.purge(limit=1)
        await message.channel.send('Pls post links in their respective advertise channels. Thank you')

    await client.process_commands(message)


@client.command()
async def dm_all(ctx, *, args=None):
    if args is not None:
        # print(ctx.author+'pinged everyone: "'+args+'"')
        if ctx.message.author.guild_permissions.administrator:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(args)
                except:
                    print('couldnt DM ' + str(member.name))
        else:
            await 
    else:
        await ctx.channel.send('no args provided')
    await ctx.message.channel.purge(limit=1)


@client.command()
async def dm(ctx, users: Greedy[User], *, mess=None):
    if users is not None and mess is not None:
        if ctx.message.author.guild_permissions.administrator:
            for user in users:
                await user.send(mess)
        else:
            ctx.channel.send('You are not allowed to use this command')
    await ctx.message.channel.purge(limit=1)


@client.command()
async def ping(ctx):
    await ctx.channel.send('pong!')


@client.command()
async def purge(ctx):
    await ctx.purge

client.run('Your Token Here')
