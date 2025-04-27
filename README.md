# Project Title
A Haunted Circus - NeoPixel fading + DC motor + NeoPixel ring control project using MicroPython.

# Components Used
- ESP32 board
- NeoPixel LED strip (10 LEDs)
- DC Motor
- Motor Driver (L298N)
- Jumper Wires
- Breadboard
- Power Supply (external)

# Setup
- Connect the NeoPixel strip data pin to GPIO4.
- Connect the DC motor via L298N to GPIO12, GPIO13, GPIO15.
- Power the motor driver externally.
- Flash MicroPython firmware to ESP32.

# Code
See Final_Code (DC+NeoRing+NeoStrip).py for full code.

## Notes
- Be careful with motor voltage and current.
- Ensure common ground for ESP32 and Motor Driver.
