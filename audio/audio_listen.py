import time
import keyboard
import pyaudio
import numpy as np
from reuseable.configs import MobileConfig


def audio_intensity(sample_rate=44100, chunk_size=1024):
    """
    Records audio from the default input device and calculates the intensity of the sound in decibels (dB).
    It prints the timestamp and the sound intensity in dB to the console.
    The recording can be stopped by pressing the 'insert' key.

    Parameters:
        sample_rate (int, optional): The sample rate of the audio recording in Hertz (Hz). Default is 44100 Hz.
        chunk_size (int, optional): The number of audio frames per buffer to read. Default is 1024 frames.
    """
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
                        input=True, frames_per_buffer=chunk_size)

    Threshold_value = 150
    try:
        while True:
            first_time = time.time()
            if keyboard.is_pressed('insert'):
                break
            data = np.frombuffer(stream.read(chunk_size), dtype=np.int16)
            timestamp = time.time()
            # Calculate the average absolute amplitude (sound intensity)
            sound_intensity = np.abs(data).mean()
            # sound_intensity = np.max(np.abs(data))

            if sound_intensity > Threshold_value:
                tup_audio = (sound_intensity, timestamp)
                MobileConfig.audio_det.append(tup_audio)
            print(f"{timestamp} - Sound Intensity: {sound_intensity:.2f} dB")
    except KeyboardInterrupt:
        print("Program stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

# audio_intensity()