#1 /usr/bin/python
import RPi.GPIO as GPIO
import sys


ledPins = [17,18,27,22,23,24,25,2,3,8]

pin = sys.argv[2]
int_pin = int(pin)
pin_num = ledPins[int_pin]        

if (sys.argv[1] == 'on'):
    switch = GPIO.LOW
else:
    switch = GPIO.HIGH
    
def setup():
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
        
        GPIO.output(pin_num, switch)

if __name__ == '__main__':
    setup()
    try:
        loop()
    
    except KeyboardInterrupt: #checks for cntrl + C
        destroy()
    
    