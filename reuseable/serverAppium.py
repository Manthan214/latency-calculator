import os
import subprocess
import time
from reuseable.configs import MobileConfig

def start_server():
    os.system(f" start /B start cmd.exe @cmd /k appium -p {MobileConfig.port} -a {MobileConfig.IP} ")
    #The start command is used to start a new command prompt window in the background (/B flag),
    # and the cmd.exe command is used to start a new instance of the command prompt.
    # The @cmd /k part of the command is used to tell the command prompt to run the appium command with the specified parameters.


def stop_server():
    cmd = f"netstat -ano -p tcp | findstr :{MobileConfig.port}"
    output = subprocess.check_output(cmd, shell=True)
    print(output.decode().strip().split()[-1])
    pid = int(output.decode().strip().split()[-1])
    # Kill the Appium server process with the PID
    cmd = f"taskkill /F /PID {pid}"
    subprocess.run(cmd, shell=True)
    time.sleep(5)


