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
    # return "//android.widget.ImageView[@content-desc='black_white_1.mp4']"
    # return "//android.widget.ImageView[@content-desc='video 1 [4 - 0.5].mp4']"
    return "//android.widget.ImageView[@content-desc='Video_Audio_11.mp4']"
    # return "//android.widget.ImageView[@content-desc='video 2 [4.5- 0.5].mp4']"
    # return "//android.widget.ImageView[@content-desc='video_3.mp4']"
    # return "//android.widget.ImageView[@content-desc='video with white noise.mp4']"
    # return "//android.widget.ImageView[@content-desc='video_1_black_white.mp4']"


