import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

out_pin = 4
GPIO.setup(out_pin, GPIO.OUT)

motor = GPIO.PWM(out_pin, 50)

motor.start(0)


# motor.ChangeDutyCycle([2.5 ~ 12]) -90~90
motor.ChangeDutyCycle(2.5)
time.sleep(0.5)

motor.ChangeDutyCycle(7.25)
time.sleep(0.5)

motor.stop()
GPIO.cleanup()
