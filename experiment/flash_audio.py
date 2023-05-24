import time

import serial.tools.list_ports
from testScripts import testVideo
import pyfirmata
import speech_recognition as sr
from reuseable.configs import MobileConfig
import simple_colors

def arduino():
    # for x in range(10):

    board = [p.device for p in serial.tools.list_ports.comports() if 'USB-SERIAL' in p.description]
    port = pyfirmata.Arduino(board[0])
    pin = port.get_pin('a:3:i')
    led = port.get_pin('d:8:o')
    it = pyfirmata.util.Iterator(port)
    it.start()
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
        # time.sleep(1)
        if read_out is not None:
            if (read_out>0.1):
                led.write(1)
                MobileConfig.flash.append(start_time)
                print("Flash detected :True")
                print('Timestamp of Flash detected:', start_time)
                print("Flash detection :", read_out*1000)
                y = 0
            else:
                led.write(0)
                y+=1


r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")


Threshold_value=1000
def audio_return():
    """
    Continuously listens for sound input from the microphone and returns the timestamp when a sound is detected.

    Returns:
    float: Timestamp of the sound detection.

    Raises:
    IOError: If there is an issue with the microphone.
    """
    a=0
    print("----intilizing the microphone----")
    while True:
        if a>5:
            break
        with m as source:
            r.adjust_for_ambient_noise(source)
            print(r.energy_threshold)
            if r.energy_threshold>Threshold_value:
                sound_time = time.time()
                MobileConfig.audio_det.append(sound_time)
                a=0
                print("True")
                print("----Timestamp of sound detect:",sound_time,"----")
                time.sleep(1)
            else:
                a+=1
        # print("Set minimum energy threshold to {}".format(r.energy_threshold))
