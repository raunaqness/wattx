import time
import sys
import paho.mqtt.client as paho
import json
import random

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker")
    sys.exit(-1)

"""
Script to generate random sensor readings values
"""

for i in range(5000):
    data = {
        "sensorID": f"sensor-{random.randint(1, 3)}",
        "type": "temperature",
        "value": random.randint(15, 30),
    }
    print(data)
    client.publish("/readings/temperature", json.dumps(data), 0)
    time.sleep(1)

client.disconnect()
