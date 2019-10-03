import RPi.GPIO as GPIO
import time
import sys

ledPins = [17,18,27,22,23,24,25,2,3,8]
pin_string = sys.argv[1]
pin_int = int(pin_string)
arg_index = ledPins.index(pin_int)
pin = ledPins[arg_index]

if (sys.argv[2] == 'on'):
    switch = GPIO.LOW
else:
    switch = GPIO.HIGH


def setup():
    print("Program is starting......")
    GPIO.setmode(GPIO.BCM)
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        
        
def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()
    
    
def loop():
    while True:
        GPIO.output(pin, switch)

        
if __name__ == '__main__':
    setup()
    try:
        loop()
    
    except KeyboardInterrupt: #checks for cntrl + C
        destroy()
    
    