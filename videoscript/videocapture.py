from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
video_filename = "/home/pi/Desktop/EntropEYE-Camera/fotocapture/video_{}.h264".format(timestamp)

print("Start recording...")
camera.start_recording(video_filename)
camera.wait_recording(30)
camera.stop_recording()

!MP4Box -add video_filename.h264 video_filename.mp4
print("Done.")
