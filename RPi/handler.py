from report_parser import parse
import json

class Handler:
    def __init__(self):
        pass

    def mqtt_setup(self, mqtt):
        self.mqtt = mqtt

    def publish_report(self, topic):
        self.mqtt.set_topic(topic)
        report_json = json.dumps(self.report)
        self.mqtt.publish(report_json)

    def open_file(self, file_name):
        self.file = open(file_name, "a")

    def close_file(self):
        self.file.close()

    def write_to_file(self):
        self.file.write(self.data.hex()+"\n")

    def print_report(self):
        print()
        print(self.data.hex())
        print(self.report)

    def report_handle(self, data, thing_id):
        self.data = data
        #self.write_to_file()
        self.thing_id = thing_id
        self.report = parse(self.data.hex(), self.thing_id)

        if "TMP" in self.report:
            self.print_report()
            self.publish_report(self.thing_id+"/env1")
        if "AMB" in self.report:
            self.print_report()
            self.publish_report(self.thing_id+"/env2")
        if "BTN" in self.report:
            self.print_report()
            self.publish_report(self.thing_id+"/btn")
