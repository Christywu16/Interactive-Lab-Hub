import time
import board
import busio
import adafruit_mpr121
import pygame
import qwiic_joystick

#weather api
from requests import get
import json
from pprint import pprint

import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from datetime import date
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
from pydub import AudioSegment


pygame.mixer.init()

myJoystick = qwiic_joystick.QwiicJoystick()
myJoystick.begin()


i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

#weather date
today = date.today()
print(today.day)
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

# weather API
key = '087bd0646cd970da00b4911cbdb2f8da'
url = 'https://api.openweathermap.org/data/2.5/weather?lat=40&lon=-73.95&appid=087bd0646cd970da00b4911cbdb2f8da'

# Get weather and temperature 
weather = get(url).json()['weather'][0]['main']
temp = str(round((get(url).json()['main']['temp']- 273.15),2))
temperature = temp
temp = 'Temperature: ' + temp

# Days left to Christmas, play text to speech
daysLeft = str(24 - today.day)
print(today.day)
mytext = "Today is December" + str(today.day) + "th" + "  There's" + daysLeft + " days to Christmas. The current weather is " + weather + " and the current temperature is " + temperature + "Celsius"
print(mytext)
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")

song = AudioSegment.from_mp3("welcome.mp3")
song.export("welcome.wav", format="wav")
weather_sound = pygame.mixer.Sound('welcome.wav')
  
# # Playing the converted file
# os.system("mpg321 welcome.mp3")

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

while True:
    # show date, weather, and tempreture on pi screen
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    cmd = "hostname -I | cut -d' ' -f1"
    IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    y = top
    draw.text((x, y), d4, font=font, fill="#FFFFFF")
    y += font.getsize(d4)[1]
    draw.text((x, y), weather, font=font, fill="#00FF00")
    y += font.getsize(IP)[1]
    draw.text((x, y), temp, font=font, fill="#FFFF00")
    y += font.getsize(temp)[1]
    
    
    disp.image(image, rotation)
    time.sleep(0.1)

    # For 12 touch sensor point, each has an assigned Christmas Song
    for i in range(12):
        # while point 1 receives data from touch sensor
        if i == 1:
            if mpr121[i].value:
                # if user touch the current date
                # play today's weather
                if (today.day == i):
                    weather_sound.play()
                # play assigned song
                playing = pygame.mixer.Sound('happy-christmas-party.wav').play()
                # pull joystick downwards to stop song
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(5)
                    pygame.time.delay(5)
        elif i == 2:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('1_141009.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 3:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('And Its Christmas.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 4:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('christmas-vacation.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 5:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('gq0210_0848447Atx.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 6:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('jingle-bells.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 7:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('I Heard The Bells On Christmas Day.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 8:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('magical-fairy-tale.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 9:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('santa-is-coming.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 10:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('Twelve 12 Days Of Christmas.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 11:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('When Christmas Comes to Town.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        elif i == 0:
            if mpr121[i].value:
                if (today.day == i):
                    weather_sound.play()
                playing = pygame.mixer.Sound('jingle-bells.wav').play()
                while playing.get_busy():
                    if myJoystick.horizontal == 0:
                        playing.stop()
                    time.sleep(.5)
                    pygame.time.delay(100)
        
            
            
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
    