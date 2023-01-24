#!/usr/local/bin/python3

DEBUG = False

REQUEST_TIMEOUT = 10

# MQTT client
BROKER = "localhost"
PORT = 1883
TOPIC = "Telldus/Control"


# Telldus Local API
API = 'http://192.168.0.30/api/'
HEADERS = {'Authorization': 'Bearer xxxx'}