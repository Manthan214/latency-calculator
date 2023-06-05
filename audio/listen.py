import threading

import speech_recognition as sr
import datetime
from testScripts import testVideo
import time
from reuseable.configs import MobileConfig
import simple_colors

r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")

aud_tup = []
Threshold_value = 200
global event
event=threading.Event()
class audio():
    def adjust(self, event: threading.Event) -> None:
        while True:
            with m as source:
                r.adjust_for_ambient_noise(source)
            if event.is_set():
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
        print("----intilizing the microphone----")
        while True:
            if a > 40:
                event.set()
                break

            sound_time = time.time()
            # print(r.energy_threshold)
            time.sleep(0.2)
            if r.energy_threshold >= Threshold_value:
                tup_audio = (r.energy_threshold, sound_time)
                aud_tup.append(tup_audio)
                a = 0
                print("True")
                print("----Timestamp of sound detect:", sound_time, "----")
                # time.sleep(1)
            else:
                a += 1
            # print("Set minimum energy threshold to {}".format(r.energy_threshold))

    def listen(self):
        """
            Uses the microphone to listen for speech input and returns the recognized text.

            Returns:
            str: The recognized text from the speech input.

            Raises: SpeechRecognitionError: If the speech input cannot be recognized or if there is an issue with the
            microphone.
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



if __name__=="__main__":
    tt = audio()
    y = threading.Thread(target=tt.adjust,args=(event,))
    y.start()
