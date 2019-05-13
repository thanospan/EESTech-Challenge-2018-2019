from bluepy.btle import Peripheral, DefaultDelegate
import time

class MyDelegate(DefaultDelegate):
    def __init__(self, per):
        DefaultDelegate.__init__(self)
        self.per = per

    def handleNotification(self, ch_hnd, data):
        if ch_hnd == self.per.data_ch_hnd:
            self.per.handler.report_handle(data, self.per.thing_id)
        else:
            print("\nNotification: Unknown Handle")

class BleDevice:
    def __init__(self, addr, thing_id):
        self.addr = addr
        self.thing_id = thing_id

    def connect(self):
        print("--Connect")
        print(" -Connecting to Peripheral:", self.addr)
        self.per = Peripheral(self.addr)
        print(" -Connected to Peripheral:", self.addr)
        print()

    def disconnect(self):
        print("--Disconnect")
        print(" -Disconnecting from Peripheral:", self.addr)
        self.per.disconnect()
        print(" -Disconnected from Peripheral:", self.addr)

    def setup(self):
        print("--Setup")

        self.per.setMTU(112)
        print(" -MTU set to 112 bytes (109+3 bytes)")

        self.svc = self.per.getServiceByUUID("2ea78970-7d44-44bb-b097-26183f402400")

        self.data_ch = self.svc.getCharacteristics("2ea78970-7d44-44bb-b097-26183f402410")[0]
        self.data_ch_hnd = self.data_ch.getHandle()
        self.per.writeCharacteristic(self.data_ch_hnd+1, b"\x01\00", True)
        print(" -Enabled notifications on characteristic 0x2410")

        self.ctrl_ch = self.svc.getCharacteristics("2ea78970-7d44-44bb-b097-26183f402409")[0]
        self.ctrl_ch_hnd = self.ctrl_ch.getHandle()
        self.ctrl_ch.write(b"\x01", True)
        print(" -Wrote 0x01 to characteristic 0x2409")

        self.per.withDelegate( MyDelegate(self) )
        print()

    def set_handler(self, handler):
        self.handler = handler

    def print_svc_char(self):
        print("--Services and Characteristics")
        services = self.per.getServices()
        for svc in services:
            print(svc)
            print(svc.uuid)
            print()
            characteristics = svc.getCharacteristics()
            for char in characteristics:
                print("\t", char)
                print("\t", char.uuid)
                print("\t Handle:", char.getHandle())
                print("\t", char.propertiesToString())
                print()

    def get_data(self, mins):
        print("--Reports")
        t_end = time.time() + 60 * mins
        while time.time() < t_end:
            if self.per.waitForNotifications(1.0):
                continue
            print(" -Waiting...")
        print()
