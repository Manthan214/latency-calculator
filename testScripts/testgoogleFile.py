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


def launch_appium_driver():
    """
    Launches the Appium driver and starts the VLC player app on the connected device or emulator.

    Raises:
    WebDriverException: If there is an issue with launching the Appium driver or starting the specified app.
    """
    global driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", MobileConfig.desired_caps)
    driver.implicitly_wait(10)
    driver.start_activity("com.google.android.apps.nbu.files", ".home.HomeActivity")
    time.sleep(3)


def play_video():
    driver.find_element(AppiumBy.XPATH, videoLocators.browse()).click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, videoLocators.gVideo()).click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, videoLocators.image_video()).click()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(377, 727)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


# launch_appium_driver()
# play_video()
