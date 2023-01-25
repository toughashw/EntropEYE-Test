import RPi.GPIO as GPIO
import time
import picamera
import telegram

# configurazione sensore HC-SR04
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

# configurazione camera
camera = picamera.PiCamera()

# configurazione Telegram Bot
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

while True:
    # invia un trigger al sensore HC-SR04
    GPIO.output(23, True)
    time.sleep(0.00001)
    GPIO.output(23, False)
    
    # inizio e fine del segnale
    start = time.time()
    stop = time.time()
    
    # attesa del segnale di ritorno
    while GPIO.input(24) == 0:
        start = time.time()
    
    while GPIO.input(24) == 1:
        stop = time.time()
    
    # calcola la distanza
    elapsed = stop - start
    distance = (elapsed * 34300) / 2
    
    # se la distanza è inferiore a 10 cm, cattura una foto e un video
    if distance < 10:
        camera.start_preview()
        time.sleep(2)
        camera.capture('image.jpg')
        camera.start_recording('video.h264')
        time.sleep(5)
        camera.stop_recording()
        camera.stop_preview()
        
        # converti video in mp4
        !MP4Box -add video.h264 video.mp4
        
        # invia foto e video a Telegram Bot
        bot.send_photo(chat_id='YOUR_CHAT_ID', photo=open('image.jpg', 'rb'))
        bot.send_video(chat_id='YOUR_CHAT_ID', video=open('video.mp4', 'rb'))