import time

import serial.tools.list_ports
from reuseable.configs import MobileConfig
from testScripts import testVideo
import pyfirmata

lst1 = []
lst2 = []
lst3 = []


# def arduino():
#     """
#     Initializes the communication with an Arduino board connected to the computer via USB-SERIAL port and returns a serial connection to an Arduino board connected via USB.
#
#     Returns:
#     ser (serial.Serial): Serial connection object for communicating with the Arduino board.
#     """
#     print("----intilizing the arduino----")
#     board=[p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
#     ser = serial.Serial(board[0], 9600)
#
#     print("----intilizing Complete ----")
#     return ser
# def getArduino(pin):
#         """
#         Reads data from the given serial object `pin` connected to an Arduino, calculates the value, and
#         prints the presence of(whether or not) a flash was detected along with the timestamp and the calculated value. It also adds
#         the calculated value to the global dictionary `testVideo.dict` with the key `"flash detection"`.
#
#         Args:
#         pin: A serial object connected to an Arduino
#         """
#         ouy=[]
#         y=0
#         while True:
#             x=0
#             if y>5:
#                 break
#             else:
#                 global start_time
#                 # time.sleep(1)
#                 # for i in range(5):
#                 #     if i==4:
#                 start_time = time.time()
#                 a = pin.readline()
#                 str_rn = a.decode()
#                 print(str_rn)
#
#                 #     ouy.append(str_rn)
#                 # for i in ouy:
#                 #    x+=int(i)
#
#                 # x=x/len(ouy)
#                 if int(str_rn)>=100:
#                     MobileConfig.flash.append(start_time)
#                     print("Flash detected :True")
#                     print('Timestamp of Flash detected:', start_time)
#                     print("Flash detection :", x)
#                     testVideo.dict["flash detection"] = x
#                     y = 0
#
#                 else:
#                     y+=1
#
# a=arduino()
# getArduino(a)



def arduino():
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
            if (read_out>0.15):
                led.write(1)
                MobileConfig.flash.append(start_time)
                print("Flash detected :True")
                print('Timestamp of Flash detected:', start_time)
                print("Flash detection :", read_out*1000)
                y = 0
            else:
                led.write(0)
                y+=1


#
# x,l=arduino()
# getArduino(x,l)