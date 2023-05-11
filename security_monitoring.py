# import smtplib
import time
import RPi.GPIO as GPIO  # biblioteka za ulaz i izlaz GPIO pinova
# import numpy as np
# import cv2
import discord
from picamera import PiCamera
import picamera
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents

print("Hello, this is my project!")

# učitavanje varijable okruženja iz .env datoteke
load_dotenv()

# postavljanje GPIO pinova za senzor pokreta
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# postavljanje kamere - trenutna greška u kodu s obziom na faleći ribbon kabel za kameru
# camera = picamera.PiCamera()
# camera.resolution = (640, 480)


# postavljanje discord klijenta
intents = Intents.default()  # postavljanje zadanog skupa namjeri
intents.members = True  # ova linija koda dopusta botu da prima clanove dogadjaja

bot = commands.Bot(command_prefix='!', intents=intents)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

# funkcija za detekciju pokreta


def MOTION(PIR_PIN):
    print("Otkriveno kretanje!")

    # snimanje slike sa kamerom
    filename = 'security_pic.jpg'
    camera.capture(filename)

    # slanje slike na discord kanal
    channel = bot.get_channel(int(CHANNEL_ID))
    with open(filename, 'rb') as fp:
        picture = discord.File(fp, filename=filename)
        message = "Otkriveno kretanje, provjeri privitak!"
        await channel.send(message, file=picture)
    os.remove(filename)
