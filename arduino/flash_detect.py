import time

import serial.tools.list_ports

from testScripts import testVideo
import pyfirmata

lst1 = []
lst2 = []
lst3 = []


def arduino():
    print("----intilizing the arduino----")
    board=[p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
    ser = serial.Serial(board[0], 9600)

    print("----intilizing Complete ----")
    return ser
def getArduino(pin):
        ouy=[]
        x=0
        print("----in the reading mode---")
        global start_time
        for i in range(5):
            if i==3:
                start_time = time.time()
            a = pin.readline()
            str_rn = a.decode()
            # print(str_rn)
            ouy.append(str_rn)
        for i in ouy:
           x+=int(i)

        x=x/len(ouy)
        if int(x)>=100:
            print("Flash detected :True")
            print('Timestamp of Flash detected:', start_time)
            print("Flash detection :", x)
            testVideo.dict["flash detection"] = x

# #
# ser=arduino()
# for i in range(1):
#     # it = pyfirmata.util.Iterator(port)
#     # it.start()
#     time.sleep(1)
#     getArduino(ser)
#     # print(read_out)