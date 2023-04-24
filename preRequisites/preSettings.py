import threading
import time

from arduino import flash_detect
from audio import listen
from reuseable import serverAppium
from testScripts import testVideo

def pre_req():
    # try:
    serverAppium.start_server()
    try:
        testVideo.launch_appium_driver()
    except:
        pass
        pin,port=flash_detect.arduino()
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

    testVideo.close_app()

pre_req()