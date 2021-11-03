import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sys
import json
from time import sleep

import config

publish.single(
    'countdown', 
    sys.argv[1], 
    qos=0, 
    retain=False, 
    hostname=config.MQTT_HOST, 
    port=config.MQTT_PORT, 
    client_id="", 
    keepalive=60,
    will=None,
    auth={'username':config.MQTT_AUTH["username"],'password':config.MQTT_AUTH["password"]},
    tls=None,
    protocol=mqtt.MQTTv311,
    transport="tcp",
    )
