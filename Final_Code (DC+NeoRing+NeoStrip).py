import machine
import neopixel
from time import sleep, sleep_ms

# DC MOTOR SETUP
in1 = machine.Pin(12, machine.Pin.OUT)
in2 = machine.Pin(13, machine.Pin.OUT)
ena = machine.Pin(15, machine.Pin.OUT)

in1.value(1)
in2.value(0)
ena.value(1)

# LED Strip setup (fade in/out red)
strip_pin = machine.Pin(4)
num_leds = 10
strip = neopixel.NeoPixel(strip_pin, num_leds)

# LED Ring setup (rotating two red LEDs)
ring_pin = machine.Pin(5)
ring_leds = 16
ring = neopixel.NeoPixel(ring_pin, ring_leds)

# Animation index for ring
ring_index = 0

while True:
    # Fade In
    for brightness in range(0, 256, 5):
        # Update LED strip
        strip.fill((brightness, 0, 0))
        strip.write()

        # Update LED ring
        ring.fill((0, 0, 0))
        ring[ring_index] = (255, 0, 0)
        ring[(ring_index + 1) % ring_leds] = (255, 0, 0)
        ring.write()

        ring_index = (ring_index + 1) % ring_leds
        sleep_ms(20)

    # Fade Out
    for brightness in range(255, -1, -5):
        # Update LED strip
        strip.fill((brightness, 0, 0))
        strip.write()

        # Update LED ring
        ring.fill((0, 0, 0))
        ring[ring_index] = (255, 0, 0)
        ring[(ring_index + 1) % ring_leds] = (255, 0, 0)
        ring.write()

        ring_index = (ring_index + 1) % ring_leds
        sleep_ms(20)


