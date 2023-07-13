import threading
from pydub import AudioSegment

import speech_recognition as sr
from testScripts import testVideo
import time
import keyboard
from reuseable.configs import MobileConfig

r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")

aud_tup = []
Threshold_value = 200
global event
event=threading.Event()
audio_data_t = []
audio_data_v =[]
class audio(object):
    def adjust(self, event: threading.Event) -> None:
        """
        Continuously adjusts audio for ambient noise.

        This method continuously adjusts the audio for ambient noise using the `adjust_for_ambient_noise` function from
        the `r` object. It runs in a loop until the `event` is set.

        Args:
            event (threading.Event): A threading event that signals when to stop adjusting the audio.

        Returns:
            None
        """
        while True:
            with m as source:
                r.adjust_for_ambient_noise(source)
            if event.is_set():
                break
            elif keyboard.is_pressed('space'):
                break


    def audio_return(self):
        """
        Continuously listens for sound input from the microphone and returns the timestamp when a sound is detected.

        Returns:
        float: Timestamp of the sound detection.

        Raises:
        IOError: If there is an issue with the microphone.
        """
        a = 0
        print("----Initializing microphone----")
        while keyboard.is_pressed('space') == False:
            if a > 800:
                event.set()
                break

            sound_time = time.time()
            print(r.energy_threshold)
            time.sleep(0.00002)
            if r.energy_threshold >= Threshold_value:
                tup_audio = (r.energy_threshold, sound_time)
                if len(MobileConfig.audio_det)>0:
                    if sound_time-((len(MobileConfig.audio_det)-1)[1])>=2:
                        MobileConfig.audio_det.append(tup_audio)
                else:
                    MobileConfig.audio_det.append(tup_audio)


                a = 0
                print("True")
                print("----Timestamp of sound detect:", sound_time, "----")

            else:
                a += 1

    def listen(self):
        """
            Uses the microphone to listen for speech input and returns the recognized text.

            Returns:
            str: The recognized text from the speech input.

            Raises: SpeechRecognitionError: If the speech input cannot be recognized or if there is an issue with the
            microphone.
        """
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


def audio_p():
    tt = audio()
    y = threading.Thread(target=tt.adjust,args=(event,))
    y.start()
    tt.audio_return()

