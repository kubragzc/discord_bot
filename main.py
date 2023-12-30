import discord
from bot_mantik import gen_pass


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Merhaba {client.user}! ben bir botum!')
    elif message.content.startswith('$bye'):
        await message.channel.send("Görüşürüz")
    elif message.content.startswith("/pass"):
        await message.channel.send(gen_pass(15))
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5 
        await message.channel.send("he" * count_heh)
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
