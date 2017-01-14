from pubnub import Pubnub
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
#vypnem upozornenia od GPIO
GPIO.setwarnings(False)
#nastavim si piny, ktore idem pouzivat. GPIO.OUT  znamena, ze dany pin nebude citat data ale poslielat energiu
#zelena
pin = 40
GPIO.setup(pin,GPIO.IN)
GPIO.setup(pin,GPIO.OUT)
pubnub = Pubnub(
    publish_key = "YOUR-PUBLISH-KEY",
    subscribe_key = "YOUR-SUBSCRIBE-KEY")
channel = "YOUR-CHANNEL"
GPIO.output(pin,GPIO.LOW)
status = False
def callback(message, channel):
    print('[' + channel + ']: ' + str(message))
    if message == 1:
	state = GPIO.input(pin)
	if state == 0:
    		print"turn on"
		GPIO.output(pin,GPIO.HIGH)
	else:
		print "turn off"
		GPIO.output(pin, GPIO.LOW)

pubnub.subscribe(
    channel,
    callback = callback)
quit()
