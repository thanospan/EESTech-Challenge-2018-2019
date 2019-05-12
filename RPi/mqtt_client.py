import paho.mqtt.client as paho
import time

class MqttClient():
    def __init__(self, broker_addr, port, client_name):
        self.broker_addr = broker_addr
        self.port = port
        self.client_name = client_name
        
        self.client = paho.Client(client_name)
        
        #Bindings
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        
    def on_connect(self, client, userdata, flags, rc):
        if rc==0:
            print(" -Connected to MQTT broker:", self.broker_addr)
        else:
            print(" -Could not establish connection:", rc)
        print()
        
    def on_disconnect(self, client, userdata, rc):
        if rc==0:
            print(" -Disconnected from MQTT broker:", self.broker_addr)
        else:
            print(" -Error while disconnecting:", rc)
            
    def connect(self):        
        print(" -Connecting to MQTT broker:", self.broker_addr)
        self.client.connect(self.broker_addr, self.port)
        self.client.loop_start()
        time.sleep(1)
        
    def disconnect(self):
        print("\n -Disconnecting from MQTT broker:", self.broker_addr)
        self.client.loop_stop()
        self.client.disconnect()
        time.sleep(1)
        
    def setTopic(self, topic):
        self.topic = topic
        
    def publish(self, payload):
        self.client.publish(self.topic, payload, 0, True)