from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)
camera.resolution = (1920, 1080)
camera.vflip = True
camera.contrast = 10

 timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    picture_filename = "/home/pi/Desktop/EntropEYE-Camera/fotocapture/picture_{}.jpg".format(timestamp)

camera.capture(picture_filename)
print("Done.")
