import discord
import asyncio
import random
import os
from discord.ext import commands
from requests import async

 
TOKEN = ''
API_ENDPOINT = 'https://opentdb.com/api.php?amount=10&category=31&difficulty=easy'
 
client = discord.Client()
 
prefix = "."
bot = commands.Bot(command_prefix=prefix)
count = 0

commands = {
    ".hello": 'Oi galerinha!',
    ".joinha": 'Dá um joinha aí, por favor!',
    ".devinha": 'Com certeza é a julinha!',
    ".teclas": '!@#$%¨&*(()_+/?°₢°ºª§ª:;><',
    ".comandos": '.hello, .pm, .tilt, .joinha, .devinha, .teclas, Tudo bom, Mike?, .dado',
}

# words = { 'Tudo bom' , 'Como vai' , 'Salve' , 'Oi' , 'Olá' }

def select_answer(response):
    item = random.choice(response.data.results)
    await message.channel.send(item.question)

@client.event
async def on_message(message):
    global count

    if message.author == client.user:
        return

    print(message.content)
    
    key = message.content
    if key in commands:
        answer = commands[key]
        await message.channel.send(answer)
    
    if message.content.startswith('.pm'):
        await message.channel.send(f'latency {client.latency}')
   
    if message.content.startswith('.tilt'):
        count += 1
        await message.channel.send(f"EU TO TILTADA CARA? {count}")
 
    if message.content.startswith('.dado'): 
        numr = random.randint(1,6)
        await message.channel.send(str(numr))
        return

    if message.content.startswith('Tudo bom, Mike?'):
        answer = random.choice(['Não respondo a isso','Sim','As vezes','Não','Claro','NUNCA!','Um dia talvez','A resposta está dentro de ti','Mais ou menos','Uma Bosta','Podia ser pior'])
        await message.channel.send(answer)
        return
    
    if message.content.startswith('.pergunta'):
        await async.get(API_ENDPOINT, hooks = {'response' : select_answer})
        return

    # typed = message.content

    # if typed.lower().find('mike') != -1:
    #     for i in words:
    #         if typed.find(i) != -1:
    #             await message.channel.send('funcionou')
    #             break

@client.event
async def on_ready():
    game = discord.Game(name='A Júlia é god')
    await client.change_presence(status=discord.Status.online, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)


