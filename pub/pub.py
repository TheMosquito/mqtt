import paho.mqtt.publish as publish
import datetime
import time

TOPIC = "/topic"
SLEEP = 5

while True:
  msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  publish.single(TOPIC, payload=msg, qos=0, hostname="broker", port=1883)
  print("Sent:     topic:" + TOPIC + ", msg:" + msg)
  time.sleep(SLEEP)

