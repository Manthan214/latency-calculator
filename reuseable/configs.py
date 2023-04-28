import subprocess


def get_device_udid():
    cmd = "adb devices -l"
    output = subprocess.check_output(cmd.split())
    devices = output.decode().strip().split("\n")[1:]
    if len(devices) == 1:
        return devices[0].split()[0]
    else:
        de = []
        for device in devices:
            if "device" in device:
                de.append(device.split()[0])
        return de[0]

def get_android_version():
    cmd = "adb shell getprop ro.build.version.release"
    output = subprocess.check_output(cmd.split())
    version = output.decode().strip()
    return version

def get_device_name():
    cmd = "adb shell getprop ro.product.model"
    output = subprocess.check_output(cmd.split())
    name = output.decode().strip()
    return name


class MobileConfig:
    port = 4723
    IP = "0.0.0.0"

    desired_caps = {
        'deviceName': 'Pixel 2',
        'platformName': 'Android',
        'platformVersion': '11',
        'udid': get_device_udid()
    }
