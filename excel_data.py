from testScripts import testVideo
from audio import listen
import pandas as pd
dict_excel = {'Listen_start': [], 'Video_play': [], 'flash detection': [], 'Video_pause': [], 'Listen_stop': [],
              'start_diff': []}


def difference():
    start_difference = float(testVideo.dict['Video_play']) - float(testVideo.dict['Listen_start'])
    testVideo.dict["start_diff"] = start_difference

    for j in dict_excel.keys():
        dict_excel[j].extend([testVideo.dict[j]])

def excel_disp():
    df = pd.DataFrame(dict_excel)
    df.to_excel("output_final.xlsx", index=False)
    # stop_difference = testVideo.dict['Video_pause'] - testVideo.dict['Listen_stop']
    # testVideo.dict["stop_diff"] = stop_difference