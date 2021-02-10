# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

class Publisher:
	def __init__(self):
		self._client = mqtt.Client()

	def publish(self, broker_adress, topic, message):
		self._client.connect(broker_adress)
		self._client.publish(topic, message)
		self._client.disconnect()


class Subscriber:
	def __init__(self):
		self._client = mqtt.Client()
		self._broker_adress = 0
		self._topic = 0 

	def connect_4ever(self, broker_adress, topic):

		def on_message(client, userdata, msg):
			print(msg.payload.decode())

		def on_connect(client, userdata, flags, rc):
			print("Connected with result code "+str(rc))
			self._client.subscribe(self._topic)

		self._broker_adress = broker_adress
		self._topic = topic

		self._client.on_connect = on_connect
		self._client.on_message = on_message
		
		self._client.connect(broker_adress)
		self._client.loop_forever()
