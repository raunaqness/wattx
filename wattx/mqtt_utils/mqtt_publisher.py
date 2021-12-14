
import json
import paho.mqtt.client as paho

from django.conf import settings

mqtt_config = settings.MQTT_CONFIG

class MQTTPublisher:
    def __init__(self):
        self.client = paho.Client()
        if self.client.connect(mqtt_config['HOST'], mqtt_config['PORT'], mqtt_config['TIMEOUT']) != 0:
            print("Could not connect to MQTT Broker")
            
    
    def publish(self, topic: str, payload: dict) -> bool:
        """
        Function to publish message to given dict payload to mqtt topic
        """
        
        try:
            self.client.publish(topic, json.dumps(payload))
            return True
        except:
            return False
        
