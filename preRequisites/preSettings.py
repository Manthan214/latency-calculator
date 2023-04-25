import threading
import time

from arduino import flash_detect
from audio import listen
from reuseable import serverAppium
from testScripts import testVideo

def pre_req():
    # try:
    print("launching appium server")
    serverAppium.start_server()
    try:
        print("launching app ")
        testVideo.launch_appium_driver()
    except:
        pass
    print("initializing pin and port with arduino")
    pin,port=flash_detect.arduino()
    # for i in range(5):
    print("threading")
    thread3 = threading.Thread(target=listen.audio_return)
    thread3.start()
    thread1 = threading.Thread(target=testVideo.play_video)
    thread1.start()
    thread2 = threading.Thread(target=flash_detect.getArduino,args=(pin,port))
    thread2.start()
    time.sleep(5)

    thread5 = threading.Thread(target=testVideo.pauseVideo)
    thread5.start()
    thread5.join()

    thread1.join()
    thread2.join()
    thread3.join()
    print("itration complete.......{}")
    time.sleep(1)

    testVideo.close_app()
    return pin,port
# pre_req()