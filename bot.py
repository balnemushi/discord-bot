import discord
from discord.ext import commands
import os
import threading
from flask import Flask

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 간단한 명령어 예시
@bot.command()
async def 안녕(ctx):
    await ctx.send("안녕하세요 저는 바알네무시 마크1 입니다! 👋")

# =============== Flask 웹서버 부분 ===============
app = Flask(__name__)

@app.route('/')
def index():
    return "봇이 실행 중입니다!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

# =============== 실행 ===============
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run(os.environ["DISCORD_TOKEN"])
