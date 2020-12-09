import typing
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Load .env for Auth token
load_dotenv()

# Declare the Intent to use the `on_member_join` event
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix="w!",
    intents=intents
)

with open('text/welcome_message.txt', 'r') as w:
    welcome_message = ''.join(w.readlines())


@bot.event
async def on_ready():
    print(f"{bot.user} connected to Discord!")


@bot.event
async def on_member_join(member):
    # Find a channel called `welcome`
    welcome_channel = discord.utils.get(member.guild.text_channels, name='welcome')
    # If it doesn't exist, set it to the first channel in the listing
    if not welcome_channel:
        welcome_channel = member.guild.text_channels[0]
    await welcome_channel.send(welcome_message.replace('@', member.mention))


@bot.command(help="Get user avatar")
async def avatar(ctx, member: typing.Optional[discord.Member] = None):
    if not member:
        member = ctx.author
    await ctx.send(f"{member.mention}'s Profile Picture:")
    await ctx.send(member.avatar_url)


bot.run(os.environ["DISCORD_AUTH_TOKEN"])
