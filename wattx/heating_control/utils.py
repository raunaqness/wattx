import json
import random

from django.db.models import Avg

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
    Helper function to calculate openness level of valve for a given "roomID"
    Logic - 
        1. get current temperature reading of all sensors in a given "roomID"
        2. get the average temperature value
        3. calculate the absolute difference -> temp_diff = abs(average_temperature - 22) since 22 is target
        4. calculate % of openness required -> openness_percentage = (temp_diff / 22) * 100
    
    """
    
    try:
        qs = Sensor.objects.filter(room__roomID=roomID).aggregate(Avg('value'))
        average_temperature = round(float(qs['value__avg']), 2)
        temperature_difference = abs(average_temperature - 22)
        openness_percentage = (temperature_difference / 22) * 100
        
        # openness value can be max 100%
        openness_percentage = min(openness_percentage, 100)
        
        print(f"average_temperature : {average_temperature}")
        print(f"openness_percentage : {openness_percentage}")
        
        return openness_percentage
    
    except:
        print(f"Error occurred while calculating openness value for roomID : {roomID}")
        return Valve.object.filter(room__roomID=roomID).first().level
    
    