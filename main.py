import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random
import webserver

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome, {member.name} to the server! Enjoy your stay and watch out for Techmarine.")
    guild = member.guild
    role = discord.utils.get(guild.roles, name="Member")
    if role:
        await member.add_roles(role)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "juno" in message.content.lower() and random.random() < 0.5:
        await message.channel.send("Juno is green.")
    await bot.process_commands(message)

webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
