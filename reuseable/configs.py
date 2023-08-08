import subprocess


def get_device_udid():
    """Get the UDID of the connected Android device using ADB.

    This method uses ADB (Android Debug Bridge) to retrieve the UDID (Unique Device Identifier) of the connected Android device. It runs the 'adb devices -l' command and parses the output to find the UDID.

    Returns:
        str or None: The UDID of the connected Android device, or None if no device is connected or if the UDID cannot be determined.
    """
    cmd = "adb devices -l"
    output = subprocess.check_output(cmd.split())
    devices = output.decode().strip().split("\n")[1:]
    if len(devices) == 1:
        return devices[0].split()[0]
    else:
        for device in devices:
            if "device" in device:
                return device.split()[0]
    return None


def get_android_version():
    """Get the Android version of the connected device using ADB.

    This method uses ADB (Android Debug Bridge) to retrieve the Android version of the connected device. It runs the 'adb shell getprop ro.build.version.release' command and captures the output, which represents the Android version.

    Returns:
        str: The Android version of the connected device.
    """
    cmd = "adb shell getprop ro.build.version.release"
    output = subprocess.check_output(cmd.split())
    version = output.decode().strip()
    return version


class MobileConfig:
    port = 4723
    IP = "0.0.0.0"
    flash = []
    audio_det = []
    pin = 'a:3:i'
    led = 'd:8:o'
    Threshold_flash = 0.2
    Threshold_audio = 0.15

    desired_caps = {
        'deviceName': 'Pixel 2',
        'platformName': 'Android',
        'platformVersion': get_android_version(),
        'udid': get_device_udid()
    }
