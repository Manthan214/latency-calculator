class MobileConfig:
    port = 4723
    IP = "0.0.0.0"

    desired_caps = {
        'deviceName': 'Pixel 2',
        'platformName': 'Android',
        'platformVersion': '11',
        'udid': 'HT81Y1A02145',
        # 'appPackage':'org.videolan.vlc',
        # 'appActivity' :'org.videolan.vlc.StartActivity'
        # 'appActivity': '.gui.MainActivity'
    }