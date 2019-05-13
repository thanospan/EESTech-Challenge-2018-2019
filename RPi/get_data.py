from ble_device import BleDevice
from mqtt_client import MqttClient
from handler import Handler

mac = "xx:xx:xx:xx:xx:xx"
thing_id = "1"

ip = "xxx.xxx.xxx.xxx"
port = 1883
client_name = "Client"

#file_name = "data.txt"
minutes = 0.5

thing = BleDevice(mac, thing_id)
mqtt = MqttClient(ip, port, client_name)
handler = Handler()

thing.connect()
mqtt.connect()

handler.mqtt_setup(mqtt)
#handler.open_file(file_name)
#thing.print_svc_char()
thing.setup()
thing.set_handler(handler)

thing.get_data(minutes)

thing.disconnect()
mqtt.disconnect()
#handler.close_file()