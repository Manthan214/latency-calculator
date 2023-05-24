import base64
import os
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from reuseable.configs import MobileConfig
from locators import videoLocators
from locators import audioLocators

global dt
global time_now
dict = {}


# Launching appium driver here
def launch_appium_driver():
    """
    Launches the Appium driver and starts the VLC player app on the connected device or emulator.

    Raises:
    WebDriverException: If there is an issue with launching the Appium driver or starting the specified app.
    """
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", MobileConfig.desired_caps)
    driver.implicitly_wait(10)
    driver.start_activity("org.videolan.vlc", "org.videolan.vlc.StartActivity")


# Starting screen recording
def start_record():
    """  Starts the screen recording and returns the timestamp for it."""
    driver.start_recording_screen()
    a_current_time = time.time()
    print('Timestamp of Record:', a_current_time)



def audio_click():
    """
    Performs click action and opens the audio window in vlc and clicks on the audio file

    Raises:
       WebDriverException: If there is an issue with performing the mouse click action or finding the specified element.
    """
    driver.find_element(AppiumBy.XPATH, audioLocators.audio_window()).click()
    # time.sleep(2)
    driver.find_element(AppiumBy.XPATH, audioLocators.wav_file()).click()
    print("Time Stamp of audio: ", time.time())
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(575, 1558)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    # time.sleep(10)

def audio_pause():
    """
    Performs click action to pause the audio being played

    Raises:
       WebDriverException: If there is an issue with performing the mouse click action or finding the specified element.
    """
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(538, 1686)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(2)
    driver.back()

# Playing video in VLC player
def play_video():
    """
    Finds the location of the video element in the VLC app and plays it.


    Raises:
    WebDriverException: If there is an issue with finding or interacting with the video element.
    """
    # driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Video']").click()
    driver.find_element(AppiumBy.XPATH, videoLocators.video()).click()
    b_current_time = time.time()
    dict["Video_play"] = str(b_current_time)[6:]
    print('Timestamp of play:', b_current_time)


def timeSleep():
    time.sleep(60)


def pauseVideo():
    """
        Pauses the video in the VLC app and returns the timestamp when it was paused.


        Raises:
        WebDriverException: If there is an issue with pausing the video or interacting with any UI elements.
        """
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1719)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1723)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    c_current_time = time.time()
    dict["Video_pause"]=str(c_current_time)[6:]
    print('Timestamp of Pause:', c_current_time)

    driver.back()

def stop_record():
    """
       Stops the screen recording in the VLC app using Appium and saves the recording to a file.


       Raises:
       WebDriverException: If there is an issue with stopping the recording or interacting with the device.
       """
    recording_raw = driver.stop_recording_screen()

    d_current_time = time.time()
    print('Timestamp of Stop_record:', d_current_time)
    video_name = "Recording" + driver.current_activity
    filepath = os.path.join("C:/Users/Anuj/PycharmProjects/Project(video-audio)/Recording/", video_name + ".mp4")

    with open(filepath, "wb+") as videoRecorder:
        videoRecorder.write(base64.b64decode(recording_raw))


def close_app():
    """ Closes the appium driver and quits the app."""
    driver.quit()
    print("Driver quit")



