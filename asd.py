import time
from gpiozero import Button,LED


coinslot = Button(16)
enable = LED(12)
while True:
    enable.off()