#!/bin/bash

# start mqtt subscriber as deamon
python manage.py runscript -v2 mqtt_utils.mqtt_subscriber &

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

