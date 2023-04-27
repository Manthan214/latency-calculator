import threading
import time

from arduino import flash_detect
from audio import listen
from reuseable import serverAppium
from testScripts import testVideo

def pre_req():
    # try:
    print("----Launching appium server----")
    serverAppium.start_server()
    try:
        print("----Launching app---- ")
        testVideo.launch_appium_driver()
    except:
        pass
    print("----Initializing pin and port with arduino----")
    ser = flash_detect.arduino()
    time.sleep(2)
    # for i in range(5):
    print("----PreRequisite Threading started----")
    thread3 = threading.Thread(target=listen.audio_return)
    thread3.start()
    thread1 = threading.Thread(target=testVideo.play_video)
    thread1.start()

    # flash_detect.getArduino(ser)
    # thread2 = threading.Thread(target=flash_detect.getArduino,args=ser)
    # thread2.start()
    thread2 = threading.Thread(target=flash_detect.getArduino(ser))
    thread2.start()
    time.sleep(5)

    thread5 = threading.Thread(target=testVideo.pauseVideo)
    thread5.start()

    thread5.join()
    thread1.join()
    thread2.join()
    thread3.join()
    time.sleep(1)

    testVideo.close_app()

    return ser
# pre_req()