import time
import board
import busio

import adafruit_mpr121
import pygame

pygame.mixer.init()
sound10 = pygame.mixer.Sound('christmas-vacation.wav')
# sound1 = pygame.mixer.Sound('happy-christmas-party.wav')
sound1 = pygame.mixer.Sound('jingle-bells.wav')
sound7 = pygame.mixer.Sound('santa-is-coming.wav')




i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    for i in range(12):
        print(i, mpr121[i].value)
        if i == 10:
            if mpr121[i].value:
                playing = sound10.play()
                while playing.get_busy():
                    pygame.time.delay(100)
        elif i == 1:
            if mpr121[i].value:
                playing = sound1.play()
                while playing.get_busy():
                    pygame.time.delay(100)
        elif i == 7:
            if mpr121[i].value:
                playing = sound7.play()
                while playing.get_busy():
                    pygame.time.delay(100)
            
            
    time.sleep(0.25)  # Small delay to keep from spamming output messages.
    