import discord
import asyncio
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
import json

f = open('config.json')
token = json.load(f)['token']

pre = open('config.json')
prefix = json.load(pre)['prefix']

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print('BOT on!')
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('buuuur'))

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45"}

@client.command()
async def cep(ctx, cep):
    r = requests.get(f'http://viacep.com.br/ws/{cep}/json/', headers=headers).json()
    a = r['cep']
    b = r['logradouro']
    c = r['complemento']
    d = r['bairro']
    e = r['localidade']
    f = r['uf']
    g = r['ibge']
    h = r['gia']
    i = r['ddd']
    j = r['siafi']
    embed = discord.Embed(
            title = 'CEP',
            description = (f'**cep:** {a}\n**logradouro:** {b}\n**complemento:** {c}\n**bairro:** {d}\n**localidade:** {e}\n**uf:** {f}\n**ibge:** {g}\n**gia:** {h}\n**ddd:** {i}\n**siafi:** {j}'),
            colour = discord.Colour.red()
            )

    embed.set_footer(text='by mino#2914')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/804776816485073023/821751200558743583/depositphotos_411026992-stock-illustration-logo-design-white-letter-letter.jpg')

    await ctx.send(embed=embed)


@client.command()
async def ip(ctx, ip):
    r = requests.get(f'http://ip-api.com/json/{ip}', headers=headers).json()
    a = r['country']
    b = r['region']
    c = r['regionName']
    d = r['city']
    e = r['lat']
    f = r['lon']
    g = r['isp']
    h = r['zip']
    i = r['org']
    j = r['as']
    k = r['query']
    embed = discord.Embed(
            title = 'IP',
            description = (f'**País:**  {a}\n**Região:**  {b}\n**Nome Região:**  {c}\n**Cidade:**  {d}\n**Latitude:**  {e}\n**Longitude:**  {f}\n**zip:**  {h}\n**isp:**  {g}\n**org:**  {i}\n**as:**  {j}\n\n**Ip requerido:**  {k}'),
            colour = discord.Colour.red()
            )

    embed.set_footer(text='by mino#2914')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/804776816485073023/821751200558743583/depositphotos_411026992-stock-illustration-logo-design-white-letter-letter.jpg')

    await ctx.send(embed=embed)

client.run(token)
