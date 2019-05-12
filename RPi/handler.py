from report_parser import parse
import json

class Handler:
    def __init__(self):
        pass
        
    def mqttSetup(self, mqtt):
        self.mqtt = mqtt
        
    def printReport(self):
        print()
        print(self.data.hex())
        print(self.report)
        
    def publishReport(self, topic):
        self.mqtt.setTopic(topic)
        report_json = json.dumps(self.report)
        self.mqtt.publish(report_json)
        
    def reportHandle(self, data, thingID):
        self.data = data
        self.thingID = thingID
        self.report = parse(self.data.hex(), self.thingID)
        
        if "TMP" in self.report:
            self.printReport()
            self.publishReport(self.thingID+"/env1")
        if "AMB" in self.report:
            self.printReport()
            self.publishReport(self.thingID+"/env2")
        if "BTN" in self.report:
            self.printReport()
            self.publishReport(self.thingID+"/btn")