import machine
import neopixel
import time

pin = machine.Pin(4)
num_leds = 10
np = neopixel.NeoPixel(pin, num_leds)

while True:
    for brightness in range(0, 256, 5):  # 0 to 255 in steps of 5
        for i in range(num_leds):
            np[i] = (brightness, 0, 0)
        np.write()
        time.sleep_ms(20)

    for brightness in range(255, -1, -5):  # 255 to 0 in steps of -5
        for i in range(num_leds):
            np[i] = (brightness, 0, 0)
        np.write()
        time.sleep_ms(20)
