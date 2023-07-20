import matplotlib.pyplot as plt
import pandas as pd



def calculation(a, b):
    peak = []
    for i in range(len(a)):
        if b[i] > b[0] + 3:
            if a[i] >= 0.2:
                if len(peak) > 0:
                    if abs(peak[len(peak) - 1][1] - b[i]) > 3:
                        peak.append((a[i], b[i]))
                else:
                    peak.append((a[i], b[i]))
    return peak
def calculation_a(a, b):
    peak = []
    for i in range(len(a)):
        if b[i] > b[0] + 3:
            if a[i] >= 0.15:
                if len(peak) > 0:
                    if abs(peak[len(peak) - 1][1] - b[i]) > 3:
                        peak.append((a[i], b[i]))
                else:
                    peak.append((a[i], b[i]))
    return peak
def latency(f_31_1, a_31_1):
    """Calculate latency and generate a latency plot.

    This function takes in two lists of data, `f_31_1` and `a_31_1`, calculates the latency between peaks in the data, and generates a latency plot using matplotlib.

    Args:
        f_31_1 (list): List of flash data points, where each point is represented as a tuple of value and time.
        a_31_1 (list): List of audio data points, where each point is represented as a tuple of value and time.

    Returns:
        None
        """
    lst1_v = []
    lst1_t = []
    lst2_v = []
    lst2_t = []
    threshold_f = []
    threshold_a = []
    for i in f_31_1:
        if i:
            lst1_v.append(i[0])
            lst1_t.append(i[1])
            threshold_f.append(0.5)
    # print(len(lst1_v), "flash")
    if a_31_1 is None:
        pass
    else:
        for j in a_31_1:
            if j:
                lst2_v.append(j[0])
                lst2_t.append(j[1])
                threshold_a.append(0.25)
        # print(len(lst2_v), "audio")

    max_v_f = max(lst1_v)
    scaled_f = []
    scaled_a = []
    for _ in lst1_v:
        scaled_f.append(_ / max_v_f)
    if len(lst2_v) > 0:
        max_v_a = max(lst2_v)
        for _ in lst2_v:
            scaled_a.append(_ / max_v_a)

    # peaks_a = []
    # ui = []
    # if scaled_a is not None:
    #     for i in range(1, len(scaled_a) - 1):
    #         if lst2_t[i] > lst1_t[0] + 3:
    #             if scaled_a[i] > scaled_a[i - 1] and scaled_a[i] >= scaled_a[i + 1]:
    #                 if scaled_a[i] > 0.3:
    #                     if len(peaks_a) > 0:
    #                         if abs(peaks_a[len(peaks_a) - 1][1] - lst2_t[i]) < 2:
    #                             ui.append((scaled_a[i], lst2_t[i]))
    #                             # print(ui)
    #                         if abs(peaks_a[len(peaks_a) - 1][1] - lst2_t[i]) > 2:
    #                             if len(ui) > 0:
    #                                 if ui[0] in peaks_a:
    #                                     pass
    #                                 else:
    #                                     if len(peaks_a) > 0:
    #                                         peaks_a[len(peaks_a) - 1] = ui[0]
    #                                     else:
    #                                         peaks_a.append(ui[0])
    #                                         ui = []
    #                             peaks_a.append((scaled_a[i], lst2_t[i]))
    #                     else:
    #                         peaks_a.append((scaled_a[i], lst2_t[i]))
    # # Display local peaks
    # # print("Local peaks:", peaks_a)
    # # Find local peaks
    # peaks_f = []
    # ui = []
    # for i in range(1, len(scaled_f) - 1):
    #     if lst1_t[i] > lst1_t[0] + 3:
    #         if scaled_f[i] > scaled_f[i - 1] and scaled_f[i] >= scaled_f[i + 1]:
    #             if scaled_f[i] > 0.3:
    #                 if len(peaks_f) > 0:
    #                     if abs(peaks_f[len(peaks_f) - 1][1] - lst1_t[i]) < 2:
    #                         ui.append((scaled_f[i], lst1_t[i]))
    #                         # print(ui)
    #                     if abs(peaks_f[len(peaks_f) - 1][1] - lst1_t[i]) > 2:
    #                         if len(ui) > 0:
    #                             if ui[0] in peaks_f:
    #                                 pass
    #                             else:
    #                                 if len(peaks_f) > 0:
    #                                     peaks_f[len(peaks_f) - 1] = ui[0]
    #                                 else:
    #                                     peaks_f.append(ui[0])
    #                                     ui = []
    #                         peaks_f.append((scaled_f[i], lst1_t[i]))
    #                 else:
    #                     peaks_f.append((scaled_f[i], lst1_t[i]))
    peaks_a = calculation_a(scaled_a,lst2_t)
    print("peaks_a",len(peaks_a))
    peaks_f = calculation(scaled_f,lst1_t)
    print("peaks_f",len(peaks_f))

    diff = []
    scaled_a = []
    scaled_f = []
    lst1_t = []
    lst2_t = []
    y = 0
    while y < min(len(peaks_a), len(peaks_f)):

        if abs(peaks_a[y][1] - peaks_f[y][1]) > 2:
            if abs(peaks_a[y + 1][1] - peaks_f[y][1]) < 2:
                diff.append(abs(peaks_a[y + 1][1] - peaks_f[y][1]))
                scaled_a.append(peaks_a[y + 1][0])
                scaled_f.append(peaks_f[y][0])
                lst1_t.append(peaks_f[y][1])
                lst2_t.append(peaks_a[y + 1][1])
                y += 1
            elif abs(peaks_a[y][1] - peaks_f[y + 1][1]) < 2:
                diff.append(abs(peaks_a[y][1] - peaks_f[y + 1][1]))
                scaled_a.append(peaks_a[y][0])
                scaled_f.append(peaks_f[y + 1][0])
                lst1_t.append(peaks_f[y + 1][1])
                lst2_t.append(peaks_a[y][1])
                y += 1
        elif abs(peaks_a[y][1] - peaks_f[y][1]) < 2:
            diff.append(abs(peaks_a[y][1] - peaks_f[y][1]))
            scaled_a.append(peaks_a[y][0])
            scaled_f.append(peaks_f[y][0])
            lst1_t.append(peaks_f[y][1])
            lst2_t.append(peaks_a[y][1])
            y += 1
        elif y > min(len(peaks_a), len(peaks_f)):
            break

    print(diff)

    flash_data = {'flash value': scaled_f, 'flash_time': lst1_t, 'Audio value': scaled_a, 'Audio_time': lst2_t,
                  'Latency': diff}
    fdata = pd.DataFrame(flash_data)
    writer = pd.ExcelWriter('Latency_ddata.xlsx', engine='xlsxwriter')
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
    plt.bar(x, diff, color='blue',
            width=0.4)
    plt.plot(x, diff, color='green')
    plt.title("Latency Graph")
    plt.xlabel("Number of iterations")
    plt.ylabel("Time (in milliseconds)")
    plt.show()
