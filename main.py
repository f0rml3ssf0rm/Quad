# Libraries
import RPi.GPIO as GPIO
import time
import threading
from adafruit_servokit import ServoKit

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

kit = ServoKit(channels=16)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


# FRONT RIGHT LEG

def fwd_fr_hip():
    kit.servo[7].angle = 60
    time.sleep(0.5)
    kit.servo[7].angle = 0
    time.sleep(0.5)


def fwd_fr_knee():
    kit.servo[15].angle = 45
    time.sleep(0.2)
    kit.servo[15].angle = 0
    time.sleep(0.2)


# FRONT LEFT LEG

def fwd_fl_hip():
    kit.servo[3].angle = 0
    time.sleep(0.5)
    kit.servo[3].angle = 90
    time.sleep(0.5)


def fwd_fl_knee():
    time.sleep(0.5)
    kit.servo[11].angle = 0
    time.sleep(0.3)
    kit.servo[11].angle = 45


# BACK RIGHT LEG

def fwd_br_hip():
    kit.servo[2].angle = 90
    time.sleep(0.5)
    kit.servo[2].angle = 0
    time.sleep(0.5)


def fwd_br_knee():
    time.sleep(0.5)
    kit.servo[14].angle = 45
    time.sleep(0.3)
    kit.servo[14].angle = 0


# BACK LEFT LEG

def fwd_bl_hip():
    kit.servo[1].angle = 90
    time.sleep(0.5)
    kit.servo[1].angle = 0
    time.sleep(0.5)


def fwd_bl_knee():
    kit.servo[13].angle = 45
    time.sleep(0.3)
    kit.servo[13].angle = 0
    time.sleep(0.2)


if __name__ == '__main__':

    # FRONT RIGHT LEG

    kit.servo[7].angle = 30
    kit.servo[15].angle = 60

    # FRONT LEFT LEG

    kit.servo[3].angle = 30
    kit.servo[11].angle = 0

    # BACK RIGHT LEG

    kit.servo[2].angle = 30
    kit.servo[14].angle = 60

    # BACK LEFT LEG

    kit.servo[1].angle = 30
    kit.servo[13].angle = 60

    time.sleep(3)

    # FRONT RIGHT LEG
    kit.servo[15].angle = 0

    # FRONT LEFT LEG
    kit.servo[11].angle = 60

    # BACK RIGHT LEG
    kit.servo[14].angle = 0

    # BACK LEFT LEG
    kit.servo[13].angle = 0

    time.sleep(5)
    try:
        while True:
            # dist = distance()
            # if dist >= 0:

            #    print ("Walk = %.1f cm" % dist)

            Thread1 = threading.Thread(target=fwd_fr_hip)
            Thread2 = threading.Thread(target=fwd_fr_knee)
            Thread3 = threading.Thread(target=fwd_fl_hip)
            Thread4 = threading.Thread(target=fwd_fl_knee)
            Thread5 = threading.Thread(target=fwd_br_hip)
            Thread6 = threading.Thread(target=fwd_br_knee)
            Thread7 = threading.Thread(target=fwd_bl_hip)
            Thread8 = threading.Thread(target=fwd_bl_knee)

            Thread1.start()
            Thread2.start()
            Thread3.start()
            Thread4.start()
            Thread5.start()
            Thread6.start()
            Thread7.start()
            Thread8.start()

            Thread1.join()
            Thread2.join()
            Thread3.join()
            Thread4.join()
            Thread5.join()
            Thread6.join()
            Thread7.join()
            Thread8.join()

            # else:
            #   print ("Stop = %.1f cm" % dist)
            #    time.sleep(3)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()