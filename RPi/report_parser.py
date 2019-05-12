from datetime import datetime
from math import floor

def switch(report_id):
    switcher = {
        1:("ACC", 9),
        2:("GYR", 9),
        3:("MAG", 9),
        4:("PRS", 7),
        5:("HMD", 7),
        6:("TMP", 7),
        7:("SFL", 11),
        #8:("COMMAND_REPLY",),
        9:("AMB", 7),
        10:("PRX", 7),
        11:("GAS", 7),
        12:("AQI", 7),
        13:("BTN", 7),
        #14:("VELOCITY_DELTA", 9),
        #15:("EULER_ANGLE_DELTA", 9),
        #16:("QUATERNION_DELTA", 11)
    }
    
    return switcher.get(report_id, "UNKNOWN_ID")
    
def step(L):
    report_id = L[0]
    sensor_report = []
    sensor_report.append(switch(report_id)[0])
    if report_id in [4,5,6,12]:
        report_list = L[:switch(report_id)[1]]
        report_bytes = bytes(report_list[3:])
        value = int.from_bytes(report_bytes, byteorder='little')
        if report_id in [4,6]:
            value = round(value*0.01,2)
        elif report_id == 5:
            value = round(value*0.9765*0.001,2)
        else:
            value = round(value,2)
        sensor_report.append(value)
    if report_id == 13:
        report_list = L[:switch(report_id)[1]]
        value = report_list[1]
        if value == 1:
            value = "Pressed"
        else:
            value = "Released"
        sensor_report.append(value)
    if report_id == 9:
        report_list = L[:switch(report_id)[1]]
        report_bytes = bytes(report_list[3:])
        value = int.from_bytes(report_bytes, byteorder='little')
        value = floor(value*0.25)
        sensor_report.append(value)
    if report_id == 10:
        report_list = L[:switch(report_id)[1]]
        value = report_list[3]
        if value == 1:
            value = "On"
        else:
            value = "Off"
        sensor_report.append(value)
    else:
        sensor_report.append(L[:switch(report_id)[1]])
        #sensor_report.append(L[3:switch(report_id)[1]])
    
    return sensor_report
    
def parse(string, thingID):
    if len(string) < 6:
        return {"UNKNOWN_ID": None}
    string = string[4:]
    L = [int(string[i:i+2], 16) for i in range(0, len(string), 2)]
    #print(L)
    multi_sensor_report = {}
    multi_sensor_report["TIMESTAMP"] = datetime.now().strftime("%d-%m-%Y %X")
    multi_sensor_report["THING_ID"] = thingID
    
    while True:
        report_id = L[0]
        if (switch(report_id) == "UNKNOWN_ID") or (switch(report_id)[1] > len(L)):
            return {"UNKNOWN_ID": None}
        sensor_report = step(L)
        L = L[switch(report_id)[1]:]
        multi_sensor_report[sensor_report[0]] = sensor_report[1]
        if len(L) < switch(report_id)[1]:
            break
            
    return multi_sensor_report