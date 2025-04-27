import machine
import neopixel
from time import sleep

ring_pin = machine.Pin(5)
ring_leds = 16
ring = neopixel.NeoPixel(ring_pin, ring_leds)

while True:
    for i in range(ring_leds):
        # Turn off all ring LEDs
        for j in range(ring_leds):
            ring[j] = (0, 0, 0)

        # Light one LED at a time in red
        ring[i] = (255, 0, 0)
        ring.write()

        sleep(0.1)
