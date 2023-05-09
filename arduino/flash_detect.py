import time

import serial.tools.list_ports

from testScripts import testVideo
import pyfirmata

lst1 = []
lst2 = []
lst3 = []


def arduino():
    """
    Initializes the communication with an Arduino board connected to the computer via USB-SERIAL port and returns a serial connection to an Arduino board connected via USB.

    Returns:
    ser (serial.Serial): Serial connection object for communicating with the Arduino board.
    """
    print("----intilizing the arduino----")
    board=[p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
    ser = serial.Serial(board[0], 9600)

    print("----intilizing Complete ----")
    return ser
def getArduino(pin):
        """
        Reads data from the given serial object `pin` connected to an Arduino, calculates the value, and
        prints the presence of(whether or not) a flash was detected along with the timestamp and the calculated value. It also adds
        the calculated value to the global dictionary `testVideo.dict` with the key `"flash detection"`.

        Args:
        pin: A serial object connected to an Arduino
        """
        ouy=[]
        x=0
        global start_time
        time.sleep(1)
        for i in range(5):
            if i==4:
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

