
import board
import neopixel
import time
import digitalio
import math
import array
import audioio
import touchio
from board import *

length = 8000 // 440
sine_wave = array.array("H", [1] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15) + 2 ** 15)

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
touch1 = touchio.TouchIn(A1)
touch2 = touchio.TouchIn(A2)
touch3 = touchio.TouchIn(A3)
touch4 = touchio.TouchIn(A4)
touch5 = touchio.TouchIn(A5)
touch6 = touchio.TouchIn(A6)
touch7 = touchio.TouchIn(A7)
slide_switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
slide_switch.switch_to_input(pull=digitalio.Pull.UP)
sample = audioio.AudioOut(board.SPEAKER, sine_wave)

while True:
    if slide_switch.value:
        print("Slide switch off!")
        pixels.fill((0, 0, 0))
        pixels.write()
        sample.stop()
        continue
    if touch1.value:
        print('touched 1!')
        pixels.fill((51, 0, 0))
        pixels.write()
        if not sample.playing or (
          (sample.playing and not sample.frequency == 8000)):
            sample.frequency = 8000
            sample.play(loop=True)
    elif touch2.value:
        print('touched 2!')
        pixels.fill((51, 25, 0))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 9000)):
            sample.frequency = 9000
            sample.play(loop=True)
    elif touch3.value:
        print('touched 3!')
        pixels.fill((51, 51, 0))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 10000)):
            sample.frequency = 10000
            sample.play(loop=True)
    elif touch4.value:
        print('touched 4!')
        pixels.fill((0, 51, 0))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 10800)):
            sample.frequency = 10800
            sample.play(loop=True)
    elif touch5.value:
        print('touched 5!')
        pixels.fill((0, 51, 51))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 12000)):
            sample.frequency = 12000
            sample.play(loop=True)
    elif touch6.value and not touch7.value:
        print('touched 6!')
        pixels.fill((0, 0, 51))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 13500)):
            sample.frequency = 13500
            sample.play(loop=True)
    elif touch7.value and not touch6.value:
        print('touched 7!')
        pixels.fill((25, 0, 51))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 15000)):
            sample.frequency = 15000
            sample.play(loop=True)
    elif touch6.value and touch7.value:
        print('touched 8!')
        pixels.fill((51, 0, 51))
        pixels.write()
        if not sample.playing or (
         (sample.playing and not sample.frequency == 16000)):
            sample.frequency = 16000
            sample.play(loop=True)
    else:
        pixels.fill((0, 0, 0))
        pixels.write()
        sample.stop()
