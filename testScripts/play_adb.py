import subprocess
import time
import os
# a=int(input("Enter how many seconds you want to play the video: "))
subprocess.call(["adb", "devices"])

def video_vlc():
    subprocess.call(["adb", "shell", "am", "start", "-n", "org.videolan.vlc/.StartActivity"])
    time.sleep(3)

    subprocess.call(["adb", "shell", "input", "tap", "305", "302"])
    subprocess.call(["adb", "shell", "input", "tap", "200", "205"])
    time.sleep(10)
    #
    # file_path = "/storage/emulated/0/Download/black_white.mp4"
    #
    # command = ["adb", "shell", "am", "start", "-n", "org.videolan.vlc/.StartActivity", "-d", file_path]
    # subprocess.call(command)
    # time.sleep(3)

    # To pause a video
    subprocess.call(["adb", "shell", "input", "tap", "542", "1729"])
    subprocess.call(["adb", "shell", "input", "tap", "542", "1729"])
    # time.sleep(10)
    print("Thank you!")
video_vlc()