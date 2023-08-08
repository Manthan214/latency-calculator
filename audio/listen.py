import threading
import time
import keyboard
import speech_recognition as sr
from testScripts import testVideo
from reuseable.configs import MobileConfig

r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")

aud_tup = []
THRESHOLD_VALUE = 200
event=threading.Event()

class Audio():
    """
    This class provides methods for adjusting audio settings, detecting sound input,
    and recognizing speech from a microphone source.

    """
    def adjust(self):
        """
        Continuously adjusts audio for ambient noise.

        This method continuously adjusts the audio for ambient noise using the
        `adjust_for_ambient_noise` function from
        the `r` object. It runs in a loop until the `event` is set.

        Args:
            event (threading.Event): A threading event that signals when to
            stop adjusting the audio.

        Returns:
            None
        """
        while True:
            with m as source:
                r.adjust_for_ambient_noise(source)
            if event.is_set() or keyboard.is_pressed('insert'):
                break


    def audio_return(self):
        """
        Continuously listens for sound input from the microphone and returns
        the timestamp when a sound is detected.

        Returns:
        float: Timestamp of the sound detection.

        Raises:
        IOError: If there is an issue with the microphone.
        """
        break_variable = 0
        print("----Initializing microphone----")
        while True:
            if break_variable > 800:
                event.set()
                break
            if keyboard.is_pressed('insert'):
                event.set()
                break

            # time.sleep(0.011)
            time.sleep(0.00002)
            sound_time = time.time()
            print(r.energy_threshold)
            if r.energy_threshold >= THRESHOLD_VALUE:
                tup_audio = (r.energy_threshold, sound_time)
                MobileConfig.audio_det.append(tup_audio)
                break_variable = 0
                print("True")
                print("----Timestamp of sound detect:", sound_time, "----")

            else:
                break_variable += 1

    def listen(self):
        """
            Uses the microphone to listen for speech input and returns the recognized text.

            Returns:
            str: The recognized text from the speech input.

            Raises: SpeechRecognitionError: If the speech input cannot be recognized
            or if there is an issue with the
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
                # testVideo.dict["Listen_stop"] = str(y_current_time)[6:]
                print("Listen Stopped....", y_current_time)
                print("------------------------------------------")
            text = r.recognize_google(audio_data_my)
            print("sending data..", time.time())
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
    """
    Starts a threaded audio processing routine.

    This function creates an instance of the `Audio` class and initiates two concurrent
    processes. It starts a new thread to continuously adjust audio for ambient noise
    using the `adjust` method from the `Audio` instance. Additionally, it calls the
    `audio_return` method to continuously listen for sound input from the microphone and
    return the timestamp when a sound is detected."""
    class_call = Audio()
    start_thread = threading.Thread(target=class_call.adjust,args=(event,))
    start_thread.start()
    class_call.audio_return()

# audio_p()
