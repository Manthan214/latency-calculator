import time

import serial.tools.list_ports

from testScripts import testVideo
import pyfirmata
import pandas as pd

lst1 = []
lst2 = []
lst3 = []


def arduino():
    board=[p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
    print("a: ", time.time())
    port = pyfirmata.Arduino(board[0])
    pinA0 = port.get_pin('a:0:i')
    return pinA0,port
def getArduino(pinA0,port):
        start_time = time.time()
        print("Start Time", start_time)

        lst1.append(start_time)

        pin_time = time.time()
        print("Pin Time", pin_time)
        lst2.append(pin_time)
        it = pyfirmata.util.Iterator(port)
        it.start()
        output = []

        for i in range(5):
            if i == 0:
                flash_current_time = time.time()
                print('Timestamp of Flash detected:', flash_current_time)
                lst3.append(flash_current_time)
            read_out = pinA0.read()
            output.append(read_out)
            # print(read_out)
            time.sleep(1)
        output_final = 0
        for i in output:
            print(output)
            if i is not None:
                output_final += float(i) * 1000
                print(output_final)
        output_final = output_final / (len(output) - 1)
        # port.exit()
        print("Flash detection :", output_final)
        testVideo.dict["flash detection"] = output_final


# pin,port=arduino()
# for i in range(4):
    # getArduino(pin,port)
# der = {"start func": lst1, "after pin": lst2, "flash detect": lst3}
# df = pd.DataFrame(der)
# df.to_excel("ardiuno_excel.xlsx", index=False)
# print('lst1', lst1)
# print('lst2', lst2)
# print('lst3', lst3)
