from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10

file_name = "/home/pi/Desktop/EntropEYE-Camera/videocapture/video_" + str(time.time()) + ".mp4"

print("Start recording...")
camera.start_recording(file_name)
camera.wait_recording(30)
camera.stop_recording()
print("Done.")
