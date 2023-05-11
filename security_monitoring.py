from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
import RPi.GPIO as GPIO
import numpy as np
import cv2
import discord
from picamera import PiCamera


print("Hello, this is my project!")


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

client.run('16779446')
