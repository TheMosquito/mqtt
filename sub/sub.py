import paho.mqtt.client as mqtt

TOPIC="/topic"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print("Received: topic:" + msg.topic + ", msg:" + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker", 1883, 60)
client.loop_forever()

