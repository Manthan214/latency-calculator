import matplotlib.pyplot as plt
import pandas as pd
from reuseable.configs import MobileConfig


def calculation(value, timestamp, Threshold_value):
    """
      Detects peaks in the input data and returns a list of tuples containing peak values and corresponding b-values.

      Parameters:
          value (list): List of numeric values representing data.
          timestamp (list): List of numeric values representing data.
          Threshold_value: Threshold value of the config file 

      Returns:
          list: A list of tuples with peak values from 'value' and corresponding values from 'timestamp'.
      """
    peak = []
    for i in range(len(value)):
        if timestamp[i] > timestamp[0] + 2:
            if value[i] > Threshold_value:
                if len(peak) > 0:
                    if abs(peak[len(peak) - 1][1] - timestamp[i]) > 3:
                        peak.append((value[i], timestamp[i]))
                else:
                    peak.append((value[i], timestamp[i]))
    return peak


def latency(flash, audio):
    """Calculate latency and generate a latency plot.

    This function takes in two lists of data, `flash` and `audio`, calculates the latency between peaks in the data, and generates a latency plot using matplotlib.

    Args:
        flash (list): List of flash data points, where each point is represented as a tuple of value and time.
        audio (list): List of audio data points, where each point is represented as a tuple of value and time.

    Returns:
        None
        """
    flash_value = []
    flash_time = []
    audio_value = []
    audio_time = []
    for i in flash:
        flash_value.append(i[0])
        flash_time.append(i[1])
    if audio is None:
        pass
    else:
        for j in audio:
            audio_value.append(j[0])
            audio_time.append(j[1])

    scaled_flash = []
    scaled_audio = []
    if len(flash_value) > 0:
        max_v_f = max(flash_value)
        for _ in flash_value:
            scaled_flash.append(_ / max_v_f)
    if len(audio_value) > 0:
        max_v_a = max(audio_value)
        for _ in audio_value:
            scaled_audio.append(_ / max_v_a)

    peaks_a = calculation(scaled_audio, audio_time, MobileConfig.Threshold_audio)
    print("peaks_a", len(peaks_a))
    peaks_f = calculation(scaled_flash, flash_time, MobileConfig.Threshold_flash)
    print("peaks_f", len(peaks_f))

    diff = []
    scaled_audio = []
    scaled_flash = []
    flash_time = []
    audio_time = []
    y = 0
    min1 = min(len(peaks_a), len(peaks_f))
    while y < min1:

        if y + 1 < len(peaks_a) and abs(peaks_a[y][1] - peaks_f[y][1]) > 2:
            if abs(peaks_a[y + 1][1] - peaks_f[y][1]) < 2:
                diff.append(abs(peaks_a[y + 1][1] - peaks_f[y][1]))
                scaled_audio.append(peaks_a[y + 1][0])
                scaled_flash.append(peaks_f[y][0])
                flash_time.append(peaks_f[y][1])
                audio_time.append(peaks_a[y + 1][1])
                y += 1
            elif y + 1 < len(peaks_f) and abs(peaks_a[y][1] - peaks_f[y + 1][1]) < 2:
                diff.append(abs(peaks_a[y][1] - peaks_f[y + 1][1]))
                scaled_audio.append(peaks_a[y][0])
                scaled_flash.append(peaks_f[y + 1][0])
                flash_time.append(peaks_f[y + 1][1])
                audio_time.append(peaks_a[y][1])
                y += 1
        elif abs(peaks_a[y][1] - peaks_f[y][1]) <= 2:
            diff.append(abs(peaks_a[y][1] - peaks_f[y][1]))
            scaled_audio.append(peaks_a[y][0])
            scaled_flash.append(peaks_f[y][0])
            flash_time.append(peaks_f[y][1])
            audio_time.append(peaks_a[y][1])
            y += 1
        elif y > min(len(peaks_a), len(peaks_f)):
            break

    print(diff)

    flash_data = {'flash value': scaled_flash, 'flash_time': flash_time, 'Audio value': scaled_audio, 'Audio_time': audio_time,
                  'Latency': diff}
    fdata = pd.DataFrame(flash_data)
    writer = pd.ExcelWriter('Latency_data.xlsx', engine='xlsxwriter')
    fdata.to_excel(writer, sheet_name='Data', index=False)
    writer.close()

    p = 0
    c = 0
    for _ in range(len(diff)):
        if diff[_] < 2:
            p += diff[_]
            c += 1
    if c > 0:
        print((p / c) * 1000, " milliseconds")
    else:
        print(0)
    x = [x for x in range(len(diff))]
    # # Plot the graph
    c = [0.035] * max(len(peaks_a), len(peaks_f))
    d = [0.065] * max(len(peaks_a), len(peaks_f))
    e = [0.100] * max(len(peaks_a), len(peaks_f))
    plt.plot(x, c, color='red')
    plt.plot(x, d, color='black')
    plt.fill_between(x, c, d, color="lightgray", label="Best range")
    plt.plot(x, e, color='green')
    plt.fill_between(x, d, e, color='pink', label="Average range")
    plt.bar(x, diff, color='blue',
            width=0.4)
    plt.plot(x, diff, color='orange', label='latency')
    plt.legend()
    plt.title("Latency Graph")
    plt.xlabel("Number of iterations")
    plt.ylabel("Time (in Seconds)")
    plt.show()
