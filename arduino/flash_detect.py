import time

import serial.tools.list_ports
from reuseable.configs import MobileConfig
from testScripts import testVideo
import pyfirmata

lst1 = []
lst2 = []
lst3 = []


def arduino():
    """
    Connects to an Arduino board and returns a pin and LED object.

    Returns:
        tuple: A tuple containing the pin and LED objects.

    Note:
        This function requires the `pyfirmata` library to be installed.
    """
    # for x in range(10):

    board = [p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
    port = pyfirmata.Arduino(board[0])
    pin = port.get_pin('a:3:i')
    led = port.get_pin('d:8:o')
    it = pyfirmata.util.Iterator(port)
    it.start()
    output = []
    return pin,led
def getArduino(pin,led):
    """
        Reads data from an Arduino pin and controls an LED based on the readings.

        Args:
            pin: The pin object from the Arduino board.
            led: The LED object from the Arduino board.


        """
    y=0
    while True:
        if y>7:
            break
        global start_time
        start_time=time.time()
        read_out = pin.read()
        # print(read_out)
        time.sleep(1)
        if read_out is not None:
            if (read_out>=0):
                tup_flash=(read_out,start_time)
                MobileConfig.flash.append(tup_flash)
                if read_out>0.15:
                    led.write(1)
                else:
                    led.write(0)
                if read_out>0.2:
                    y+=1
                else:
                    y=0
                print("Flash detected :True")
                print('Timestamp of Flash detected:', start_time)
                print("Flash detection :", read_out*1000)
            else:
                led.write(0)
                # y+=1


#
# x,l=arduino()
# getArduino(x,l)