import time
import RPi.GPIO as GPIO
from Adafruit_PWM_Servo_Driver import PWM
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pwm = PWM(0x40)
servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
        pulseLength = 1000000                   # 1,000,000 us per second
        pulseLength /= 60                       # 60 Hz
        print "%d us per period" % pulseLength
        pulseLength /= 4096                     # 12 bits of resolution
        print "%d us per bit" % pulseLength
        pulse *= 1000
        pulse /= pulseLength
        pwm.setPWM(channel, 0, pulse)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

def lightEventHandler(pin):     #rgb lights, run 10 times
            times = 0
            while (times < 30):
                GPIO.output(17,0)
                time.sleep(0.1)
                GPIO.output(17,1)
                GPIO.output(25,0)
                GPIO.output(24,0)
                GPIO.output(5,0)
                time.sleep(0.1)
                GPIO.output(24,1)
                GPIO.output(25,1)
                GPIO.output(5,1)
                GPIO.output(12,0)
                time.sleep(0.1)
                GPIO.output(12,1)
                times = times + 1

def main():
        RGB = [17,22,23,24,25,5,6,13,12]  #Being a try hard and setting up RGB LED's in loops
        for pin in RGB:
                GPIO.setup(pin,GPIO.OUT)
        GPIO.add_event_detect(27,GPIO.FALLING)
        GPIO.wait_for_edge(27,GPIO.BOTH)
        GPIO.add_event_callback(27,lightEventHandler)   #Setting the pi up to multitasking 2 scripts in one
        time.sleep(5)   #time for first servo to activate
        pwm.setPWM(0,1024,3072)
        pwm.setPWM(3,1024,3072)
        time.sleep(3)    #time for second servo
        pwm.setPWM(0,0,servoMin)
        pwm.setPWM(3,0,servoMin)
        GPIO.remove_event_detect(27)

GPIO.setup(20,GPIO.OUT)
GPIO.output(20,1)
door_lock= 27
GPIO.setup(door_lock,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  #need a pull down configuration
try:
        while 1<3:
                if __name__ =="__main__":
                        main()
                        time.sleep(5)
except KeyboardInterrupt:
        GPIO.cleanup()
GPIO.cleanup()
