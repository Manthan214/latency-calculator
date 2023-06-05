import threading

import speech_recognition as sr
import datetime
# from testScripts import testVideo
import time
# from reuseable.configs import MobileConfig
import simple_colors

r = sr.Recognizer()
m = sr.Microphone()
f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")

aud_tup = []
Threshold_value = 200
global z

class audio(object):
    def adjust(self):
        z=0
        while True:
            if z==0:
                with m as source:
                    r.adjust_for_ambient_noise(source)
            else:
                break
            # time.sleep(1)

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
                z = 1
                break

            sound_time = time.time()
            print(r.energy_threshold)
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
        print(aud_tup)

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


# return audio_data_my


tt = audio()
y = threading.Thread(target=tt.adjust)
# x=threading.Thread(target=tt.audio_return)
y.start()
tt.audio_return()
# x.start()

# tt.audio_return()
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
# print(time.time())
# audio_return()
# print(time.time())


# import threading
#
# import speech_recognition as sr
# import datetime
# # from testScripts import testVideo
# import time
# # from reuseable.configs import MobileConfig
# import simple_colors
#
# # import sounddevice as sd
# import asyncio
# import time
#
# r = sr.Recognizer()
# m = sr.Microphone()
#
#
# Threshold_value=200
# aud_tup=[]
#
# # async def adjust_ambient_noise(source, recognizer):
# #     await asyncio.sleep(0)  # Allow other tasks to run
# #     loop = asyncio.get_event_loop()
# #     await loop.run_in_executor(None, recognizer.adjust_for_ambient_noise, source)
# #     print("started")
# #
# # async def audio_return():
# #     """
# #     Continuously listens for sound input from the microphone and returns the timestamp when a sound is detected.
# #
# #     Returns:
# #     float: Timestamp of the sound detection.
# #
# #     Raises:
# #     IOError: If there is an issue with the microphone.
# #     """
# #     a = 0
# #     print("----initializing the microphone----")
# #
# #     while True:
# #         if a > 9:
# #             break
# #
# #         with m as source:
# #             # Asynchronously adjust for ambient noise
# #             # await asyncio.sleep(0)  # Allow other tasks to run
# #             # loop = asyncio.get_event_loop()
# #             # await loop.run_in_executor(None, r.adjust_for_ambient_noise, source)
# #             mic_thread = threading.Thread(target=adjust_ambient_noise, args=(source, r))
# #             mic_thread.start()
# #
# #             sound_time = time.time()
# #             sound_time1 = time.time()
# #             print(sound_time, sound_time1)
# #             print(r.energy_threshold)
# #
# #             if r.energy_threshold >= Threshold_value:
# #                 tup_audio = (r.energy_threshold, sound_time)
# #                 aud_tup.append(tup_audio)
# #                 a = 0
# #                 print("True")
# #                 print("----Timestamp of sound detect:", sound_time, "----")
# #             else:
# #                 a += 1
# #     mic_thread.join()
# #     print(aud_tup)
# #
# # # Usage example
# # asyncio.run(audio_return())
#
#
# r = sr.Recognizer()
#
# m = sr.Microphone()
# f = sr.AudioFile(r"C:\Users\Anuj\PycharmProjects\Project(video-audio)\audio\recorded_audio7.wav")
#
# aud_tup=[]
#
# def adjust_ambient_noise(source, recognizer):
#     with m as source:
#         recognizer.adjust_for_ambient_noise(source)
#
# def audio_return(Threshold_value):
#     """
#     Continuously listens for sound input from the microphone and returns the timestamp when a sound is detected.
#
#     Returns:
#     float: Timestamp of the sound detection.
#
#     Raises:
#     IOError: If there is an issue with the microphone.
#     """
#     a=0
#     print("----intilizing the microphone----")
#     while True:
#         if a>9:
#             break
#         with m as source:
#             sound_time = time.time()
#             mic_thread = threading.Thread(target=adjust_ambient_noise, args=(source, r))
#             mic_thread.start()
#             sound_time1 =time.time()
#             print(sound_time,sound_time1)
#             print(r.energy_threshold)
#             if r.energy_threshold>=Threshold_value:
#                 tup_audio = (r.energy_threshold,sound_time)
#                 # MobileConfig.audio_det.append(tup_audio)
#                 aud_tup.append(tup_audio)
#                 a=0
#                 print("True")
#                 print("----Timestamp of sound detect:",sound_time,"----")
#                 # time.sleep(1)
#             else:
#                 a+=1
#     print(aud_tup)
#     mic_thread.join()
#         # print("Set minimum energy threshold to {}".format(r.energy_threshold))
#
# def listen():
#     """
#         Uses the microphone to listen for speech input and returns the recognized text.
#
#         Returns:
#         str: The recognized text from the speech input.
#
#         Raises:
#         SpeechRecognitionError: If the speech input cannot be recognized or if there is an issue with the microphone.
#         """
#     # f = sr.AudioFile(r"C:\Users\158430\PycharmProjects\Assignment\project\recorded_audio.wav")
#     try:
#         with m as source:
#             x_current_time = time.time()
#             testVideo.dict["Listen_start"] = str(x_current_time)[6:]
#             print("Listen Started....", x_current_time)
#             print("------------------------------------------")
#             audio_data_my = r.listen(source)
#             y_current_time = time.time()
#             testVideo.dict["Listen_stop"] = str(y_current_time)[6:]
#             print("Listen Stopped....", y_current_time)
#             print("------------------------------------------")
#         text = r.recognize_google(audio_data_my)
#         print("sending data..", time.time())
#         end = time.time()
#         print("text:", text)
#     except sr.UnknownValueError:
#         # Speech recognition could not understand the input
#         print("Speech recognition could not understand the input.")
#     except sr.RequestError:
#         # Unable to reach the speech recognition service
#         print("Unable to reach the speech recognition service.")
#     except AssertionError:
#         pass
#
# # return audio_data_my
#
#     # # def record(audio_data_my):
#     #     # write the recorded audio to a WAV file
#     #     print("recording the file....")
#     #     with open("recorded_audio7.wav", "wb") as f:
#     #         f.write(audio_data_my.get_wav_data())
#
#     # def detect(audio_data_my):
#     # use the recognizer to transcribe the audio
#     # text = r.recognize_google(audio_data_my)
#     # print("sending data..", time.time())
#     # end = time.time()
#     # print("text:", text)
#     # print("starting time: ", start)
#     # print("ending time: ", end)
#
# # listen()
# # print(p)
# # record(audio_data_my=p)
# # detect(audio_data_my=p)
# # Threshold_value=200
# audio_return(Threshold_value)
