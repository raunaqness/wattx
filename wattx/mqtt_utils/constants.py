from heating_control.utils import update_sensor_temperature_reading

# list of topic to be subscribed
MQTT_TOPICS_TO_SUBSCRIBE = [
    ('/readings/temperature', 0),
]

MQTT_TOPIC_TO_FUNCTION_MAPPING = {
    "/readings/temperature" : update_sensor_temperature_reading
}