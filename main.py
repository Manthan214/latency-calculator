import threading
import time
import simple_colors
from arduino import flash_detect
import pandas as pd

from reuseable import serverAppium
from testScripts import testVideo
from audio import listen
import excel_data
from preRequisites import preSettings

x=True
if __name__ == '__main__':
    try:
        print("----pre setting has been called----")
        ser = preSettings.pre_req()
        print(simple_colors.green("----pre setting has been finished sucessfully----"))
    except:
        x=False
        print(simple_colors.red("----pre settings has failed!----"))
    if (x==True):
        try:
            print(simple_colors.blue("----Relauching the application----"))
            testVideo.launch_appium_driver()
        except:
            pass

        # pin,port=flash_detect.arduino()

        for i in range(0, 2):
            print("Starting the thread",i)
            thread1 = threading.Thread(target=testVideo.play_video)
            thread1.start()
            thread2 = threading.Thread(target=flash_detect.getArduino(ser))
            thread2.start()
            thread3 = threading.Thread(target=listen.listen)
            thread3.start()

            testVideo.timeSleep()

            thread5 = threading.Thread(target=testVideo.pauseVideo)

            thread5.start()
            thread5.join()
            thread1.join()
            thread2.join()
            thread3.join()
            time.sleep(5)
            print(testVideo.dict)
            excel_data.difference()

            print("....//iteration completed//....", i+1)
        testVideo.close_app()
        excel_data.excel_disp()



    else:
        print("There is an error in code!!")

    serverAppium.stop_server()
