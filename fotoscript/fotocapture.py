from picamera import PiCamera
import time
import datetime

camera = PiCamera()
time.sleep(2)
camera.resolution = (1920, 1080)
camera.vflip = True
camera.contrast = 10

timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
picture_filename = "/home/pi/Desktop/EntropEYE-Camera/fotocapture/image_{}.jpg".format(timestamp)

print("Sto scattando...")
camera.capture(picture_filename)

print("Fatto")
