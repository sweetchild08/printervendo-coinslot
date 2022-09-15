import time
from gpiozero import Button,LED
import requests


coinslot = Button(16)
enable = LED(12)


if __name__ == '__main__':
    def checksession():
        r1 = requests.get('http://localhost/cont.php?session')
        status=r1.text=='1'
        return status

    while True:
        coin = 0
        state=False
        enable.off()
        state=checksession()
        while state:
            enable.on()
            state=checksession()
            # button is pressed when pin is LOW
            if coinslot.is_pressed:
                pressed = True
                coin=coin+1
                requests.get('http://localhost/cont.php?addcoin')
                print(coin)
            time.sleep(0.01)
        
        
        time.sleep(0.1)