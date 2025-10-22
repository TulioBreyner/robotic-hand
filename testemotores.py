from pyfirmata import Arduino,SERVO
import time

board = Arduino('COM6')

pin1 = 7

board.digital[pin1].mode = SERVO

def rotateServo(pino,angle):
    board.digital[pino].write(angle)
    time.sleep(0.015)

while True:
    rotateServo(pin1,0)
    time.sleep(1)

    rotateServo(pin1,170)
    time.sleep(2)