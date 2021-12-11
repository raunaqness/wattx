import os
import sys
import django
import pdb
from django.conf import settings

import paho.mqtt.client as paho
from mqtt_utils.constants import MQTT_TOPICS_TO_SUBSCRIBE, MQTT_TOPIC_TO_FUNCTION_MAPPING

file_path = os.path.join((os.path.dirname(os.getcwd())), 'wattx')
sys.path.append(file_path)
django.setup()


# function called when a message is received
def callback_function(client, user_data, message):
    print(f"Received message from topic : {message.topic}")
    
    # call the function based on the topic name
    topic_name = message.topic
    
    # try to execute mapped function
    try:
        func = MQTT_TOPIC_TO_FUNCTION_MAPPING.get(topic_name, None)
        if not func:
            print("not found")
        else:
            print(f"Calling function {func.__name__}")
            func(message.payload.decode())
    except:
        print("Failed while executing function...")
    
    
def run():
    
    # init client
    client = paho.Client()
    client.on_message = callback_function
    mqtt_config = settings.MQTT_CONFIG
    
    # check connectivity
    if client.connect(mqtt_config['HOST'], mqtt_config['PORT'], mqtt_config['TIMEOUT']) != 0:
        print("Could not connect to MQTT Broker")
        sys.exit(-1)
        
    # subscribe to topics
    client.subscribe(MQTT_TOPICS_TO_SUBSCRIBE)
    
    # start client loop
    try:
        print("Press CTRL + C to exit...")
        client.loop_forever()
    except:
        print("Disconnecting from broker.")
        
    client.disconnect()
    