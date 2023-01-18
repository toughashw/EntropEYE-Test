from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)
camera.resolution = (1920, 1080)
camera.vflip = True
camera.contrast = 10

file_name = "/home/pi/Desktop/EntropEYE-Camera/fotocapture/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")
