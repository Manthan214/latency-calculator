import threading
import time
from arduino import flash_detect
import pandas as pd
from testScripts import testVideo
from reuseable import serverAppium
from audio import listen
import excel_data


if __name__ == '__main__':
    # try:
    serverAppium.start_server()
    try:
        testVideo.launch_appium_driver()
    except:
        pass
    for i in range(0, 3):
        thread1 = threading.Thread(target=testVideo.play_video)
        thread1.start()
        thread2 = threading.Thread(target=flash_detect.arduino)
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
        print(testVideo.dict)
        excel_data.difference()

        print("....//iteration completed//....", i+1)
    testVideo.close_app()
    excel_data.excel_disp()
    # for k in range(len(dict_excel)):
    # dict_excel['Diff_start']=dict_excel['Listen_start']-dict_excel['Video_play']

# except:
#     print("There is an error in code!!")
# finally:
# serverAppium.stop_server()
