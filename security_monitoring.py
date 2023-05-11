# import smtplib
import time
import RPi.GPIO as GPIO  # biblioteka za ulaz i izlaz GPIO pinova
# import numpy as np
# import cv2
import discord
# from picamera import PiCamera
import picamera
import os
from discord.ext import commands
from discord import Intents
from dotenv import load_dotenv

print("Hello, this is my security project!")


# učitavanje varijable okruženja iz .env datoteke
load_dotenv()

# dohvaćanje varijable okruženja
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
if DISCORD_TOKEN is None:
    print("GREŠKA: DISCORD_TOKEN nije pronađen u .env file")
    exit(1)

# postavljanje GPIO pinova za senzor pokreta
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# postavljanje kamere - trenutna greška u kodu s obziom na faleći ribbon kabel za kameru
camera = picamera.PiCamera()
camera.resolution = (640, 480)

camera.start_preview()
time.sleep(5)  # pregled na 5 sekundi
camera.stop_preview()

camera.capture('image.jpg')


# postavljanje discord klijenta
intents = Intents.default()  # postavljanje zadanog skupa namjeri
intents.members = True  # ova linija koda dopusta botu da prima clanove dogadjaja

load_dotenv()
bot = commands.Bot(command_prefix='!', intents=intents)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')


# funkcija za detekciju pokreta


async def MOTION(PIR_PIN):
    print("Otkriveno kretanje!")

    # snimanje slike sa kamerom
    filename = 'security_pic.jpg'
    camera.capture(filename)

    # slanje slike na discord kanal
    channel = bot.get_channel(int(CHANNEL_ID))
    with open(filename, 'rb') as fp:
        picture = discord.File(fp, filename=filename)
        message = "Otkriveno kretanje, provjeri snimljeni sadržaj!"
        await channel.send(message, file=picture)
    os.remove(filename)


GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)

# pokretanje Discord klijenta


@bot.event
async def on_ready():
    print('Prijavljen korisnik {0.user}'.format(bot))

bot.run(DISCORD_TOKEN)
