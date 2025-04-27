import machine
import neopixel
from time import sleep_ms

# DC MOTOR SETUP
in1 = machine.Pin(12, machine.Pin.OUT)
in2 = machine.Pin(13, machine.Pin.OUT)
ena = machine.Pin(15, machine.Pin.OUT)

# Start motor: forward direction
in1.value(1)
in2.value(0)
ena.value(1)
