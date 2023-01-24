#!/usr/local/bin/python3
import requests
import json
import paho.mqtt.client as paho

import config


def on_message(client, userdata, message):
    # print("message received " ,str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)
    received = str(message.payload.decode("utf-8"))
    print("Received: " + str(received))
    try:
        dict_received = json.loads(received)
        command = 'device/' + str(dict_received['Action'])
        payload = 'id=' + str(dict_received['id'])
        print ("API reply: " + str(telldus_request(command, config.HEADERS, payload)))
    
    except Exception:
        print("Unknown request: " + str(received))


def telldus_request(command, headers, payload):
    command_request = config.API + command
    if DEBUG:
        print(command_request)
        print(payload)

    try:
        json_data = requests.get(command_request, headers=headers, params=payload, timeout=config.REQUEST_TIMEOUT)
        dict_data = json_data.json()
        # dict_data['success'] = True
        # dict_data['message'] = 'OK'
        
    except requests.exceptions.ConnectionError:
        dict_data = {
            'success': False,
            'message': 'Connection Error'
        }
    except requests.exceptions.Timeout:
        dict_data = {
            'success': False,
            'message': 'Request timed out'
        }
    except requests.exceptions:
        dict_data = {
            'error': True,
            'message': 'Unknown error'
        }
    return dict_data
    

# command = 'device/turnOn'
# payload = 'id=19'
# print (telldus_request(command, headers, payload))

"""
{
  "id": 19,
  "Action": "turnOn"
}
"""

def main():

    client1 = paho.Client("Telldus_MQTT_control")                # create client object
    # ret= client1.publish("house/bulb1","on")                   # publish

    client1.on_message = on_message                          #assign function to callback
    client1.connect(BROKER, PORT)                                 #establish connection
    client1.subscribe(TOPIC)

    print(str("Telldus MQTT Control listening to {}:{}:{} API: {}").format(config.BROKER, config.PORT, config.TOPIC, config.API))

    client1.loop_forever()


if __name__ == "__main__":
    main()
