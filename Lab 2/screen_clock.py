import datetime
import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

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
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
# image = "drink-some-water-cartoon.webp"
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 100
x1 = 100
# x2 = 100

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font1 = ImageFont.truetype("Roboto-Light.ttf", 45)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py

    y1 = 0
    # TODO: fill in here. You should be able to look in cli_clock.py and stats.py

    draw.text((x1, y1), time.strftime("%a %d"), font=font, fill="#F4E38E")
    # draw.text((x2,y2), time.strftime("%H:%M"), font=font, fill="#FFFFF0")
    current_time = time.strftime("%H:%M")
    y = top + 30
    draw.text((x, y), current_time, font=font1, fill="#FFFFFF")
    y += font.getsize(current_time)[1]
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)

    now = datetime.datetime.now()

    if now.hour >= 8 and now.hour <= 9:
        image = Image.open("1.png")
        backlight = digitalio.DigitalInOut(board.D22)
        backlight.switch_to_output()
        backlight.value = True

        # Scale the image to the smaller screen dimension
        image_ratio = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width = image.width * height // image.height
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = image.height * width // image.width
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

        # Crop and center the image
        x = scaled_width // 2 - width // 2
        y = scaled_height // 2 - height // 2
        image = image.crop((x, y, x + width, y + height))
        disp.image(image, rotation)
        time.sleep(1)

    elif now.hour >= 9:
        image = Image.open("2.png")
        backlight = digitalio.DigitalInOut(board.D22)
        backlight.switch_to_output()
        backlight.value = True

        # Scale the image to the smaller screen dimension
        image_ratio = image.width / image.height
        screen_ratio = width / height
        if screen_ratio < image_ratio:
            scaled_width = image.width * height // image.height
            scaled_height = height
        else:
            scaled_width = width
            scaled_height = image.height * width // image.width
        image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

        # Crop and center the image
        x = scaled_width // 2 - width // 2
        y = scaled_height // 2 - height // 2
        image = image.crop((x, y, x + width, y + height))
        disp.image(image, rotation)
        time.sleep(1)

    # Button A pressed
    if buttonB.value and not buttonA.value:  # just button B pressed
        draw.rectangle((0, 0, width, height), outline="black", fill="black")
        current_time = time.strftime("%m/%d/%Y  %H:%M")
        y = top
        x = int(width/2-font.getsize(current_time)[0]/2)
        draw.text((x, y), current_time, font=font, fill="#FFFFFF")

    # Button B pressed
    if buttonA.value and not buttonB.value:
        draw.rectangle((0, 0, width, height), outline="black", fill="black")
        hour = int(time.strftime("%H"))

        statement = ""
        if hour >= 8 and hour < 11:
            message = "Good morning. Start your day with the first two cups of water"
        elif hour >= 11 and hour < 14:
            message = "Stay Hydrated! Drink the 3rd & 4th cups of water"
        elif hour >= 14 and hour < 17:
            message = "You are half way through! Keep it going for the 5th & 6th cups of water"
        elif hour >= 17 and hour < 20:
            message = "Almost There! Drink your last two cups of to finish your day"

        y = top
        x = int(width/2-font.getsize(message)[0]/2)
        draw.text((x, y), message, font=font, fill="#FFFFFF")
