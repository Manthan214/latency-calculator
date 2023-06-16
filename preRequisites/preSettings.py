import threading
import time

import simple_colors
from testScripts import testgoogleFile
from arduino import flash_detect
from reuseable import serverAppium
from testScripts import testVideo


def pre_req():
    """
        Performs the pre-requisites for running a test.

        This function launches the Appium server, initializes the pin and port with Arduino,
        starts the necessary threads for video playback and flash detection, and closes the app
        after the test.

        Returns:
            tuple: A tuple containing the Arduino serial object (ser) and the LED object (led).
        """
    # try:
    print("----Launching appium server----")
    serverAppium.start_server()
    try:
        print("----Launching app---- ")
        # testVideo.launch_appium_driver()
        testgoogleFile.launch_appium_driver()
    except:
        pass
    print("----Initializing pin and port with arduino----")
    ser,led = flash_detect.arduino()
    time.sleep(2)
    print(simple_colors.green("----Starting the process----"))
    print(simple_colors.red("----Please be silent test has been proceed----"))
    time.sleep(5)

    # thread3 = threading.Thread(target=listen.listen)
    # thread3.start()
    # thread1 = threading.Thread(target=testVideo.play_video)
    # thread1.start()
    thread1 = threading.Thread(target=testgoogleFile.play_video)
    thread1.start()
    # thread2 = threading.Thread(target=flash_detect.getArduino(ser,led))
    # thread2.start()
    time.sleep(5)

    # thread5 = threading.Thread(target=testVideo.pauseVideo)
    # thread5.start()

    # thread5.join()
    thread1.join()
    # thread2.join()
    # thread3.join()
    time.sleep(1)

    testVideo.close_app()

    return ser,led
# pre_req()