import discord 
from ollama import chat
from discord.ext import commands 
from logic import password, tabla
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.command()
async def inicio(ctx):
    await ctx.send("Hola bienvenido a discord!")
    
@bot.command()
async def suma(ctx, num1:int, num2:int):
    await ctx.send(f"La suma de {num1} + {num2} es {num1 + num2}")

@bot.command()
async def contraseña(ctx, longitud:int):
    await ctx.send(f"Tu contraseña es {password(longitud)}")
@bot.command()
async def multi(ctx, numero:int):
    await ctx.send(f"La tabla es: {tabla(numero)}")

@bot.command()
async def archivo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{file_name} con la ruta {file_url}")
    else:
        await ctx.send("Olvidaste subir el archivo :(")
historial = {}
@bot.command()
async def ia(ctx, pregunta:str):
    user_id = ctx.author.id

    if user_id not in historial:
        historial[user_id] = []
    
    historial[user_id].append({"role":"user", "content": pregunta})
    
    response = chat(
        model='gpt-oss:120b-cloud',
        messages=historial[user_id],
    )
    await ctx.send("Estoy pensando en tu respuesta!")
    historial[user_id].append({"role":"assistant", "content": response.message.content})
    print(historial)
    await ctx.send(response.message.content)
bot.run("")
