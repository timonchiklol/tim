import discord
from discord.ext import commands
from config import token
from random import choice,randint
intents = discord.Intents.default()
intents.message_content = True
import requests

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name = "ping")
async def ping(ctx):
    await ctx.send('pong')
hi = ["hi","hello","good night"]
@bot.command(name = "start")
async def start(ctx):
    a = choice(hi)
    await ctx.reply(a)

@bot.event
async def on_ready():
    print("ready")

@bot.command(name = "roll")
async def roll(ctx,arg = 6):
    roll = randint(1,int(arg))
    await ctx.reply(str(roll))

@bot.command(name = "img")
async def img(ctx):
    await ctx.reply(file=discord.File("mem1.jpeg"))

@bot.command(name="imgroll")
async def img(ctx, arg=3):
    imgroll = randint(1, int(arg))
    if imgroll == 1:
        await ctx.reply(file=discord.File("mem1.jpeg"))
    if imgroll == 2:
        await ctx.reply(file=discord.File("mem2.jpeg"))
    if imgroll == 2:
        await ctx.reply(file=discord.File("mem3.jpeg"))

@bot.command(name = "book")
async def book(ctx):
    respons = requests.get("https://fakerapi.it/api/v1/books?_quantity=1")
    result = respons.json()
    await ctx.reply(result["data"][0]["title"]+"\n"+result["data"][0]["author"]+"\n"+result["data"][0]["description"])

@bot.command(name = "free")
async def free(message):
    respons = requests.get("https://www.freetogame.com/api/games")
    result = respons.json()
    r = randint(0, len(result)-1)
    text = (result[r]["genre"]+"\n"+result[r]["short_description"]+"\n"+result[r]["game_url"])
    embed = discord.Embed(
        title = result[r]["title"],
        description = text,
        colour = discord.Colour.from_rgb(0,0,0)
    )
    embed.set_image(url = result[r]["thumbnail"])
    await message.channel.send(embed = embed)

@bot.command(name = "weather")
async def weather(message):
    respons = requests.get("https://api.weatherbit.io/v2.0/current?city=copenhagen&key=2815243302874547bca58805fad468c9&include=minutely&lang=ru")
    result = respons.json()
    text = str(result["data"]["app_temp"])+"\n"+result["data"]["weather"]["description"]
    embed = discord.Embed(
        title = "title",
        description = text,
        colour = discord.Colour.from_rgb(0,0,0)
    )
    await message.channel.send(embed = embed)
















bot.run(token)