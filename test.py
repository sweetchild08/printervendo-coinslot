import time
import RPi.GPIO as GPIO
import requests
BUTTON_GPIO = 16
if __name__ == '__main__':
    def checksession():
        r1 = requests.get('http://localhost/cont.php?session')
        status=r1.text=='1'
        return status

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    pressed = False
    coin=0
    while True:
        session=False
        session=checksession()

        while session:
            session=checksession()
            # button is pressed when pin is LOW
            if not GPIO.input(BUTTON_GPIO):
                if not pressed:
                    pressed = True
                    coin=coin+1
                    print(coin)
            # button not pressed (or released)
            else:
                pressed = False
            time.sleep(0.01)
        time.sleep(0.3)

