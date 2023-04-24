import moviepy.editor
from os import path
from pydub import AudioSegment
import subprocess


def Vid_2_Aud():
    # video = moviepy.editor.VideoFileClip("C:/Users/Anuj/Downloads/Video123.mp4")
    #
    # aud = video.audio
    # aud.write_audiofile("Audio123.mp3")
    #
    # print("--------Converted to mp3 --------")
    #
    # file_path = 'C:/Users/Anuj/PycharmProjects/Project(video-audio)/converter/Audio123.mp3'
    # dest_path = '/Internal shared storage/Download/Audio123.mp3'
    #
    # subprocess.run(['adb', 'push', file_path, dest_path], check=True)
    import subprocess
    import moviepy.editor as mp

    # Convert video to audio
    video = mp.VideoFileClip("C:/Users/Anuj/Downloads/Video123.mp4")
    audio = video.audio
    audio.write_audiofile("Audio123.mp3")
    print("--------Converted to mp3 --------")

    # Push audio file to mobile device
    file_path = 'C:/Users/Anuj/PycharmProjects/Project(video-audio)/converter/Audio123.mp3'
    dest_path = '/storage/Download/Audio123.mp3'  # Absolute path on the mobile device

    subprocess.run(['adb', 'push', file_path, dest_path], check=True)
    print("--------Pushed to mobile device--------")


def Vid_2_Wav():
    # src = "C:/Users/Anuj/Downloads/Video123.mp4"
    # dst = "Wav123.wav"
    #
    # sound = AudioSegment.from_file(src, format="mp4")
    # sound.export(dst, format="wav")
    video = moviepy.editor.VideoFileClip("C:/Users/Anuj/Downloads/Video123.mp4")

    aud = video.audio
    aud.write_audiofile("Wav123.wav")

    print("--------Converted to wav --------")


# Vid_2_Wav()
Vid_2_Aud()
