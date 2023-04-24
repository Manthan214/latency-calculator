import os
import time
from reuseable.configs import MobileConfig

def start_server():
    os.system(f" start /B start cmd.exe @cmd /k appium -p {MobileConfig.port} -a {MobileConfig.IP} > C:/Users/Anuj/PycharmProjects/Project(video-audio)/Logs/start_logs")
    #The start command is used to start a new command prompt window in the background (/B flag),
    # and the cmd.exe command is used to start a new instance of the command prompt.
    # The @cmd /k part of the command is used to tell the command prompt to run the appium command with the specified parameters.


def stop_server():
    os.system("taskkill /F /IM node.exe > C:/Users/Anuj/PycharmProjects/Project(video-audio)/Logs/nodeLogout_logs")
    os.system("taskkill /F /IM cmd.exe > C:/Users/Anuj/PycharmProjects/Project(video-audio)/Logs/cmdTerminate_Logs")

    #The /F flag is used to forcefully terminate the process, and the /IM flag is used to specify the name of the process to be terminated.

