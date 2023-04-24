import speech_recognition as sr
# import datetime
from testScripts import testVideo
import time

r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")


def listen():
    # print("A moment of silence, please...")
    # with m as source:
    #     r.adjust_for_ambient_noise(source)
    # print("Set minimum energy threshold to {}".format(r.energy_threshold))

    # f = sr.AudioFile(r"C:\Users\158430\PycharmProjects\Assignment\project\recorded_audio.wav")
    with m as source:
        # print("Speak something...", datetime.datetime.now())
        # listen for audio input from the microphone
        x_current_time = time.time()
        testVideo.dict["Listen_start"] = str(x_current_time)[6:]
        print("Listen Started....", x_current_time)
        print("------------------------------------------")
        audio_data_my = r.listen(source)
        y_current_time = time.time()
        testVideo.dict["Listen_stop"] = str(y_current_time)[6:]
        print("Listen Stopped....", y_current_time)
        print("------------------------------------------")
    # return audio_data_my

    # # def record(audio_data_my):
    #     # write the recorded audio to a WAV file
    #     print("recording the file....")
    #     with open("recorded_audio7.wav", "wb") as f:
    #         f.write(audio_data_my.get_wav_data())

    # def detect(audio_data_my):
    # use the recognizer to transcribe the audio
    text = r.recognize_google(audio_data_my)
    print("sending data..", time.time())
    end = time.time()
    print("text:", text)
    # print("starting time: ", start)
    # print("ending time: ", end)

# p=listen()
# # print(p)
# # record(audio_data_my=p)
# detect(audio_data_my=p)
