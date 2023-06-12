def vlc_app():
    """ This will return the VLC app"""
    return "//android.widget.TextView[@text= 'VLC']"


def video():
    """ this will return the Xpath of our video"""
    return "//android.widget.TextView[@text='black_white_1']"


def gVideo():
    """ This will return the Xpath of Videos in google files"""
    return "//android.widget.TextView[@text='Videos']"

def browse():
    """ This will return the Xpath of Browse in google files"""
    return "//android.widget.FrameLayout[@content-desc='Browse']/android.widget.FrameLayout/android.widget.ImageView"

def image_video():
    """ This will return the Xpath of Video"""
    return "//android.widget.ImageView[@content-desc='black_white_1.mp4']"