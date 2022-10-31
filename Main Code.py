# import libraries
import RPi.GPIO as GPIO
import time
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# Set pins as output pins , and define as PWM servo1, servo2, servo3 and servo4
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # pin 11 for servo1
GPIO.setup(17, GPIO.OUT)
servo2 = GPIO.PWM(17, 50) # pin 17 for servo2
GPIO.setup(27, GPIO.OUT)
servo3 = GPIO.PWM(27, 50) # pin 27 for servo3
GPIO.setup(22, GPIO.OUT)
servo4 = GPIO.PWM(22, 50) # pin 22 for servo4
servoMotors = {1: servo1, 2: servo2, 3: servo3, 4:servo4}
# Start PWM running on 4 servo, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)
servo3.start(0)
servo4.start(0)
# Loop to allow user to set servo angle.
# With execution of servo.stop and GPIO cleanup :)
def motorControl(motorNo, angle):
servoMotors[motorNo].ChangeDutyCycle(2 + (angle /18))
time.sleep(0.5)
servoMotors[motorNo].ChangeDutyCycle(0)
try:
while True:
motorNo = int(input("Enter the motor No.: "))
angle = float(input("Enter the angle: "))
motorControl(motorNo, angle)
finally:
# Clean things up at the end
servo1.stop()
GPIO.cleanup()
print("Goodbye!!")
