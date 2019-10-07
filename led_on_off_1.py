import RPi.GPIO as GPIO
import time
import sys

ledPins = [17,18,27,22,23,24,25,2,3,8]
pin_string = sys.argv[1]
pin_int = int(pin_string)
arg_index = ledPins.index(pin_int)
pin = ledPins[arg_index]
switch = sys.argv[2]

if (switch == 'on'):
    on_off = GPIO.LOW
else:
    
    on_off = GPIO.HIGH
    
def setup():
  
    GPIO.setmode(GPIO.BCM)
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        
        
def destroy():
    GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()
    
    
def loop():
    while True:
        time.sleep(.1)
        GPIO.output(pin, on_off)
       
        
if __name__ == '__main__':
    setup()
    try:
        loop()
    
    except KeyboardInterrupt: #checks for cntrl + C
        destroy()
    
    