from ble_device import BleDevice
from mqtt_client import MqttClient
from handler import Handler

mac = "xx:xx:xx:xx:xx:xx"
thing_id = "1"

ip = "xxx.xxx.xxx.xxx"
port = 1883
client_name = "name"

thing = BleDevice(mac, thing_id)
mqtt = MqttClient(ip, port, client_name)
handler = Handler()

thing.connect()
mqtt.connect()

handler.mqttSetup(mqtt)
#thing.printSvcChar()
thing.setup()
thing.setHandler(handler)

thing.getData(5)

thing.disconnect()
mqtt.disconnect()
