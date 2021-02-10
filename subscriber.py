from mqtt_protocol import Subscriber

def main():	
	subscriber = Subscriber()
	subscriber.connect_4ever(broker_adress= "localhost", topic="dw/demo")

if __name__ == '__main__':
	main()