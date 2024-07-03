import discord
from discord.ext import commands
from random import choice,randint
intents = discord.Intents.default()
intents.message_content = True
import random
from config import TOKEN
# Ваш токен Discord бота
TOKEN = TOKEN

# Список изображений для случайного выбора
images = [
    "https://images.pexels.com/photos/128756/pexels-photo-128756.jpeg?cs=srgb&dl=pexels-crisdip-35358-128756.jpg&fm=jpg",
    "https://i.natgeofe.com/k/b6b9720a-1b63-4d14-849e-03dd415cd806/pufferfish-closeup_16x9.jpg?w=1200",
    "https://environmentagency.blog.gov.uk/wp-content/uploads/sites/84/2022/05/prussian-carp.png"
]


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('ready')

@bot.command(name='start')
async def start(ctx):
    response = "Din portal til viden om fisk og fiskeri i Danmark: '!Vores web', '!Vores Facebook', '!Vores telefon nummer', '!fisk'"
    await ctx.send(response)

@bot.command(name='vores_web')
async def vores_web(ctx):
    response = "https://voresfisk.dk"
    await ctx.send(response)

@bot.command(name='vores_facebook')
async def vores_facebook(ctx):
    response = "https://www.facebook.com/voresfisk"
    await ctx.send(response)

@bot.command(name='vores_telefonnummer')
async def vores_telefonnummer(ctx):
    response = "+45 96 91 92 30"
    await ctx.send(response)

@bot.command(name='fisk')
async def fisk(ctx):
    rand_url = random.choice(images)
    await ctx.send(rand_url)

@bot.command(name='default')
async def default(ctx):
    response = "Jeg har ikke lært fiskesproget endnu :("
    await ctx.send(response)

# Запуск бота
bot.run(TOKEN)