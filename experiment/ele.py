import time
import keyboard
import pyaudio
import numpy as np
from reuseable.configs import MobileConfig

import datetime

def audio_intensity(sample_rate=44100, chunk_size=1024):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate,
                        input=True, frames_per_buffer=chunk_size)

    # print("Listening... Press Ctrl+C to stop.")
    Threshold_value= 200
    try:
        while True:
            time.sleep(0.00002)
            if keyboard.is_pressed('insert'):
                break
            data = np.frombuffer(stream.read(chunk_size), dtype=np.int16)
            timestamp = time.time()
            # Calculate the average absolute amplitude (sound intensity)
            # sound_intensity = np.abs(data).mean()
            sound_intensity = np.max(np.abs(data))
            if sound_intensity > Threshold_value:
                tup_audio = (sound_intensity, timestamp)
                MobileConfig.audio_det.append(tup_audio)
            print(f"{timestamp} - Sound Intensity: {sound_intensity:.2f} dB")
    except KeyboardInterrupt:
        print("Program stopped.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

# if __name__ == "__main__":
#     get_microphone_sound_intensity()