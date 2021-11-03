# import sys
from os.path import expanduser
import paho.mqtt.client as mqtt
from time import sleep
import json

from config import (
    MQTT_HOST,
    MQTT_PORT,
    MQTT_AUTH,
)

COUNTDOWN_FILE=f"{expanduser('~')}/countdown"

# try:
#     time = int(sys.argv[1])
# except:
#     print("You must provide a time in seconds as an integer to countdown from.")

# end_time = init_time + datetime.timedelta(seconds=time)

# current_time = datetime.now()
# while current_time.timestamp() < end_time.timestamp():

def on_connect(client, userdata, flags, rc):
    print(f"Connected to mosquitto with result code {rc}")
    client.subscribe("countdown")

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    try:
        time = int(message)
    except:
        return
    
    print(f"Counting down from {time}")
    while time > 0:
        mins = str(time // 60)
        secs = str(time % 60)
        value = f"T-{mins.zfill(2)}:{secs.zfill(2)}"
        file = open(COUNTDOWN_FILE, 'w')
        file.write(value)
        file.close()
        sleep(1)
        time -= 1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(
        username=MQTT_AUTH["username"],
        password=MQTT_AUTH["password"]
        )
client.connect(MQTT_HOST, MQTT_PORT, 60)

client.loop_forever()
