import threading
import time
import simple_colors

from arduino import flash_detect
from audio import audio_listen
from experiment import latency_garph, data_analysis
from reuseable import serverAppium
from reuseable.configs import MobileConfig
from testScripts import testgoogleFile

x = True
if __name__ == '__main__':
    global ser
    global led

    try:
        print("----Pre setting is being executed----")
        serverAppium.start_server()
        print("----Initializing arduino----")
        ser, led = flash_detect.arduino()
        time.sleep(2)
        print(simple_colors.green("----Pre setting has been finished sucessfully----"))
    except:
        x = False
        print(simple_colors.red("----Pre settings has failed!----"))
    if x:
        try:
            print(simple_colors.blue("----Relauching the application----"))
            testgoogleFile.launch_appium_driver()
        except:
            pass

        testgoogleFile.play_video()
        time.sleep(1)
        thread6 = threading.Thread(target=audio_listen.audio_intensity)
        thread6.start()
        thread1 = threading.Thread(target=testgoogleFile.pal)
        thread1.start()
        thread2 = threading.Thread(target=flash_detect.get_arduino, args=(ser, led))
        thread2.start()


        thread1.join()
        thread6.join()
        thread2.join()
        time.sleep(5)

        latency_garph.latency(MobileConfig.flash, MobileConfig.audio_det)
        # data_analysis.data_analy(MobileConfig.flash, MobileConfig.audio_det)


    else:
        print("There is an error in code!!")
