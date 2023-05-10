import discord
from picamera import PiCamera
from time import sleep

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!snimi'):
        camera = PiCamera()
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/slika.jpg')
        camera.stop_preview()
        await message.channel.send(file=discord.File('/home/pi/Desktop/slika.jpg'))

client.run('your_bot_token')