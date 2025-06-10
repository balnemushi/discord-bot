import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ 봇이 로그인되었습니다! {bot.user}")

@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요, 저는 발네무시 마크1 입니다! 🤖")

bot.run(os.environ["DISCORD_TOKEN"])
