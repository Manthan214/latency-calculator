import time
import keyboard
import serial.tools.list_ports
import pyfirmata
from reuseable.configs import MobileConfig


def arduino():
    """
    Connects to an Arduino board and returns a pin and LED object.

    Returns:
        tuple: A tuple containing the pin and LED objects.

    Note:
        This function requires the `pyfirmata` library to be installed.
    """

    board = [p.device for p in serial.tools.list_ports.comports() if 'USB Serial' or 'USB-SERIAL' in p.description]
    port = pyfirmata.Arduino(board[0])
    pin = port.get_pin(MobileConfig.pin)
    led = port.get_pin(MobileConfig.led)
    iteration = pyfirmata.util.Iterator(port)
    iteration.start()
    return pin, led


def get_arduino(pin, led):


    """
        Reads data from an Arduino pin and controls an LED based on the readings.

        Args:
            pin: The pin object from the Arduino board.
            led: The LED object from the Arduino board.


        """
    break_variable = 0
    while True:
        # if y > 200:
        #     break
        if keyboard.is_pressed('insert'):
            break
        time.sleep(0.025)
        read_out = pin.read()
        start_time = time.time()
        if read_out is not None:
            if read_out >= 0:
                tup_flash = (read_out, start_time)
                MobileConfig.flash.append(tup_flash)
                if read_out > 0.15:
                    led.write(1)
                else:
                    led.write(0)
                if read_out > 0.2 or read_out == 0:
                    break_variable += 1
                else:
                    break_variable = 0
                print("Flash detected :True")
                print('Timestamp of Flash detected:', start_time)
                print("Flash detection :", read_out * 1000)
            else:
                led.write(0)
