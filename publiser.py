#!/usr/bin/env python3
import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost")
client.publish("dw/demo", "Hello world!");
client.disconnect();