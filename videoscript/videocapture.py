from picamera import PiCamera
import time
import datetime

camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10

timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
video_filename = "/home/pi/Desktop/EntropEYE-Camera/videocapture/video_{}.h264".format(timestamp)

print("Sto registrando...")
camera.start_recording(video_filename)
camera.wait_recording(30)
camera.stop_recording()

!MP4Box -add video_filename.h264 video_filename.mp4
print("Fatto")
