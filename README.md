## Telldus MQTT Control

This script controls smart devices via TellStick local API via messages published on MQTT.

##### You will need:
* Telldus Live account
* Telldus TellStick ZNet Lite V2 or similar
* Windows, Mac or Linux with Python 3 and Internet access
* An MQTT broker, for example Mosquitto

#### Settings
Edit the config.py file and add your Tellstick IP, API token and MQTT settings.

#### Usage
Publish json in topic "Telldus/Control" in the following format:

{
  "id": 19,
  "Action": "turnOn"
}

Knowing the device ID is required. Available actions are turnOn and turnOff.