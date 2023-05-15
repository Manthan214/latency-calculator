import speech_recognition as sr
# import datetime
from testScripts import testVideo
import time
from reuseable.configs import MobileConfig
import simple_colors

r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")


Threshold_value=1000
def audio_return():
    """
    Continuously listens for sound input from the microphone and returns the timestamp when a sound is detected.

    Returns:
    float: Timestamp of the sound detection.

    Raises:
    IOError: If there is an issue with the microphone.
    """
    a=0
    print("----intilizing the microphone----")
    while True:
        if a>5:
            break
        with m as source:
            r.adjust_for_ambient_noise(source)
            print(r.energy_threshold)
            if r.energy_threshold>Threshold_value:
                sound_time = time.time()
                MobileConfig.audio_det.append(sound_time)
                a=0
                print("True")
                print("----Timestamp of sound detect:",sound_time,"----")
                time.sleep(1)
            else:
                a+=1
        # print("Set minimum energy threshold to {}".format(r.energy_threshold))

def listen():
    """
        Uses the microphone to listen for speech input and returns the recognized text.

        Returns:
        str: The recognized text from the speech input.

        Raises:
        SpeechRecognitionError: If the speech input cannot be recognized or if there is an issue with the microphone.
        """
    # f = sr.AudioFile(r"C:\Users\158430\PycharmProjects\Assignment\project\recorded_audio.wav")
    try:
        with m as source:
            x_current_time = time.time()
            testVideo.dict["Listen_start"] = str(x_current_time)[6:]
            print("Listen Started....", x_current_time)
            print("------------------------------------------")
            audio_data_my = r.listen(source)
            y_current_time = time.time()
            testVideo.dict["Listen_stop"] = str(y_current_time)[6:]
            print("Listen Stopped....", y_current_time)
            print("------------------------------------------")
        text = r.recognize_google(audio_data_my)
        print("sending data..", time.time())
        end = time.time()
        print("text:", text)
    except sr.UnknownValueError:
        # Speech recognition could not understand the input
        print("Speech recognition could not understand the input.")
    except sr.RequestError:
        # Unable to reach the speech recognition service
        print("Unable to reach the speech recognition service.")
    except AssertionError:
        pass

# return audio_data_my

    # # def record(audio_data_my):
    #     # write the recorded audio to a WAV file
    #     print("recording the file....")
    #     with open("recorded_audio7.wav", "wb") as f:
    #         f.write(audio_data_my.get_wav_data())

    # def detect(audio_data_my):
    # use the recognizer to transcribe the audio
    # text = r.recognize_google(audio_data_my)
    # print("sending data..", time.time())
    # end = time.time()
    # print("text:", text)
    # print("starting time: ", start)
    # print("ending time: ", end)

# listen()
# print(p)
# record(audio_data_my=p)
# detect(audio_data_my=p)
