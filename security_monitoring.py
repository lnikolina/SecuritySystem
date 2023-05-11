# import smtplib
import time
import RPi.GPIO as GPIO  # biblioteka za ulaz i izlaz GPIO pinova
# import numpy as np
# import cv2
import discord
# from picamera import PiCamera
import picamera
import os
from dotenv import load_dotenv
from discord.ext import commands

print("Hello, this is my project!")

# učitavanje varijable okruženja iz .env datoteke
load_dotenv()

# postavljanje GPIO pinova za senzor pokreta
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

# postavljanje kamere
camera = picamera.PiCamera()
camera.resolution = (640, 480)
