import base64
import os
import threading
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from reuseable.configs import MobileConfig
from locators import videoLocators

global dt
global time_now
dict = {}


# Launching appium driver here
def launch_appium_driver():
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", MobileConfig.desired_caps)
    driver.implicitly_wait(10)
    driver.start_activity("org.videolan.vlc", "org.videolan.vlc.StartActivity")


# Starting screen recording
def start_record():
    driver.start_recording_screen()
    a_current_time = time.time()
    print('Timestamp of Record:', a_current_time)


# Opening the VLC player from menu list
def action_click():
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(542, 1598)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(549, 763)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    driver.find_element(AppiumBy.XPATH, videoLocators.vlc_app()).click()

def audio_click():
    driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Audio']").click()
    # time.sleep(2)
    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="1_to_20.wav"]').click()
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
    # driver.find_element(AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc='Video']").click()
    driver.find_element(AppiumBy.XPATH, videoLocators.video()).click()
    b_current_time = time.time()
    dict["Video_play"] = str(b_current_time)[6:]
    print('Timestamp of play:', b_current_time)


def timeSleep():
    time.sleep(10)


def pauseVideo():
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
    recording_raw = driver.stop_recording_screen()

    d_current_time = time.time()
    print('Timestamp of Stop_record:', d_current_time)
    video_name = "Recording" + driver.current_activity
    filepath = os.path.join("C:/Users/Anuj/PycharmProjects/Project(video-audio)/Recording/", video_name + ".mp4")

    with open(filepath, "wb+") as videoRecorder:
        videoRecorder.write(base64.b64decode(recording_raw))


def close_app():
    driver.quit()
    print("Driver quit")



