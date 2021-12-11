import json
import random

from heating_control.models import Sensor, Valve
from heating_control.constants import MQTT_TOPIC_NAME_VALVE_LEVEL_UPDATE
from mqtt_utils.mqtt_publisher import MQTTPublisher


def update_sensor_temperature_reading(payload):
    """
    Helper function to update temperature value of sensor received via a message 
    in MQTT topic '/reading/temperature'
    """
    try:
        data = json.loads(payload)
        
        # update value of sensor
        sensor = Sensor.objects.filter(sensorID=data['sensorID']).first()
        sensor.value = data['value']
        sensor.save()
        
        # update value of valve
        roomID = "room-1"
        recalculate_valve_level(roomID)
            
    except:
        print("Failed to update value of sensor in update_sensor_temperature_reading()")
    
    
def recalculate_valve_level(roomID: str):
    """
    Helper function to update Valve level calculate for a given roomID and send it to
    MQTT topic '/actuators/<roomID>'
    """
    
    try:
        # recalculate value
        level = get_updated_valve_value(roomID=roomID)
        
        # save to db
        valve = Valve.objects.filter(room__roomID=roomID).first()
        valve.level = level
        valve.save()
        
        # send to topic
        topic_name = f"{MQTT_TOPIC_NAME_VALVE_LEVEL_UPDATE}/{roomID}"
        payload = {
            "level": level
            }
        client = MQTTPublisher()
        client.publish(topic_name, payload)
    except:
        print(f"Failed to update valve level for roomID : {roomID}")
    

def get_updated_valve_value(roomID):
    """
    Helper function to recalculate openness level of valve for a given "roomID"
    """
    # TODO
    return random.randint(10, 40)
    
    