def vlc_app():
    """ This will return the VLC app"""
    return "//android.widget.TextView[@text= 'VLC']"


def video():
    """ this will return the Xpath of our video"""
    return "//android.widget.TextView[@text='black_white_1']"


def gVideo():
    return "//android.widget.TextView[@text='Videos']"

def browse():
    return "//android.widget.FrameLayout[@content-desc='Browse']/android.widget.FrameLayout/android.widget.ImageView"

def image_video():
    return "//android.widget.ImageView[@content-desc='black_white_1.mp4']"