import time

import serial.tools.list_ports

from testScripts import testVideo
import pyfirmata

lst1 = []
lst2 = []
lst3 = []


def arduino():
    board=[p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
    port = pyfirmata.Arduino(board[0])
    pinA0 = port.get_pin('a:0:i')
    return pinA0,port
def getArduino(pinA0,port):
        global flash_current_time
        start_time = time.time()
        lst1.append(start_time)

        pin_time = time.time()
        lst2.append(pin_time)
        it = pyfirmata.util.Iterator(port)
        it.start()
        output = []

        for i in range(5):
            if i == 3:
                flash_current_time = time.time()
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
                # print(output_final)
        output_final = output_final / (len(output) - 1)
        port.exit()
        if output_final>=200:
            print("Flash detected :True")
            print('Timestamp of Flash detected:', flash_current_time)
            print("Flash detection :", output_final)
            testVideo.dict["flash detection"] = output_final


# for i in range(5):
#     pin,port=arduino()
#     getArduino(pin,port)