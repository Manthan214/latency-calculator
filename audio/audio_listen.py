# import time
# import keyboard
# import pyaudio
# import numpy as np
# from reuseable.configs import MobileConfig
#
#
# def audio_intensity(sample_rate=44100, chunk_size=1024):
#     """
#     Records audio from the default input device and calculates
#     the intensity of the sound in decibels (dB).
#     It prints the timestamp and the sound intensity in dB to the console.
#     The recording can be stopped by pressing the 'insert' key.
#
#     Parameters:
#         sample_rate (int, optional): The sample rate of the audio recording
#         in Hertz (Hz). Default is 44100 Hz.
#         chunk_size (int, optional): The number of audio frames per buffer
#         to read. Default is 1024 frames.
#     """
#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
#                         input=True, frames_per_buffer=chunk_size)
#     break_variable = 0
#     threshold_value = 150
#     try:
#         while True:
#             if keyboard.is_pressed('insert'):
#                 break
#             # if y>200:
#             #     break
#             data = np.frombuffer(stream.read(chunk_size), dtype=np.int16)
#             timestamp = time.time()
#             # Calculate the average absolute amplitude (sound intensity)
#             # sound_intensity = np.abs(data).mean()
#             sound_intensity = np.max(np.abs(data))
#
#             if sound_intensity > threshold_value:
#                 tup_audio = (sound_intensity, timestamp)
#                 MobileConfig.audio_det.append(tup_audio)
#                 break_variable = 0
#             else:
#                 break_variable += 1
#             print(f"{timestamp} - Sound Intensity: {sound_intensity:.2f} dB")
#     except KeyboardInterrupt:
#         print("Program stopped.")
#
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
# # audio_intensity()


import time
import keyboard
import pyaudio
import numpy as np
from reuseable.configs import MobileConfig


class Configs:
    """
    Setting up the configurations for audio stream
    """
    SAMPLE_RATE = 44100
    CHUNK_SIZE = 1024
    THRESHOLD_VALUE = 150
    BREAK_KEY = 'insert'


class AudioIntensityRecorder:
    """
        Records sound intensity using a microphone stream and detects audio events
        exceeding a certain threshold. The detected audio events are stored in the
        MobileConfig class.
    """
    def __init__(self):
        """
        Initialize the AudioIntensityRecorder by creating a PyAudio instance and
        initializing the stream as None.
        """
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def open_stream(self):
        """
        Opens the microphone stream for capturing audio input.
        """
        self.stream = self.audio.open(
            format=pyaudio.paInt16, channels=1, rate=Configs.SAMPLE_RATE,
            input=True, frames_per_buffer=Configs.CHUNK_SIZE
        )

    def close_stream(self):
        """
        Close the audio stream if it's open.
        """
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

    def record_audio_intensity(self):
        """
        Continuously record audio intensity and detect audio events exceeding
        the predefined threshold. Detected events are stored in the MobileConfig class.
        """
        try:
            while True:
                if keyboard.is_pressed(Configs.BREAK_KEY):
                    break

                data = np.frombuffer(self.stream.read(Configs.CHUNK_SIZE), dtype=np.int16)
                sound_intensity = np.max(np.abs(data))
                timestamp = time.time()

                if sound_intensity > Configs.THRESHOLD_VALUE:
                    MobileConfig.audio_det.append((sound_intensity, timestamp))

                print(f"{timestamp} - Sound Intensity: {sound_intensity:.2f} dB")
        except KeyboardInterrupt:
            print("Program stopped.")
        finally:
            self.close_stream()
            self.audio.terminate()

# if __name__ == "__main__":
#     recorder = AudioIntensityRecorder()
#     recorder.open_stream()
#     recorder.record_audio_intensity()
