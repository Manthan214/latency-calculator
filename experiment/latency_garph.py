import matplotlib.pyplot as plt
import pandas as pd

def latency(f_31_1,a_31_1):
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
    print(len(lst1_v), "flash")
    if a_31_1 is None:pass
    else:
        for j in a_31_1:
            if j:
                lst2_v.append(j[0])
                lst2_t.append(j[1])
                threshold_a.append(0.25)
        print(len(lst2_v), "audio")

    max_v_f = max(lst1_v)
    scaled_f = []
    scaled_a = []
    for _ in lst1_v:
        scaled_f.append(_ / max_v_f)
    if len(lst2_v)>0 :
        max_v_a = max(lst2_v)
        for _ in lst2_v:
            scaled_a.append(_ / max_v_a)
    flash_data = {'flash value': scaled_f, 'flash_time': lst1_t}
    audio_data = {'Audio value': scaled_a, 'Audio_time': lst2_t}
    fdata = pd.DataFrame(flash_data)
    adata = pd.DataFrame(audio_data)
    writer = pd.ExcelWriter('raw_data.xlsx', engine='xlsxwriter')
    fdata.to_excel(writer, sheet_name='Flash', index=False)
    adata.to_excel(writer, sheet_name='Audio', index=False)
    writer.close()


    peaks_a = []
    ui = []
    if scaled_a is not None:
        for i in range(1, len(scaled_a) - 1):
            if lst2_t[i] > lst1_t[0] + 3:
                if scaled_a[i] > scaled_a[i - 1] and scaled_a[i] >= scaled_a[i + 1]:
                    if scaled_a[i] > 0.3:
                        if len(peaks_a) > 0:
                            if abs(peaks_a[len(peaks_a) - 1][1] - lst2_t[i]) < 2:
                                ui.append((scaled_a[i], lst2_t[i]))
                                # print(ui)
                            if abs(peaks_a[len(peaks_a) - 1][1] - lst2_t[i]) > 2:
                                if len(ui) > 0:
                                    if ui[0] in peaks_a:
                                        pass
                                    else:
                                        if len(peaks_a) > 0:
                                            peaks_a[len(peaks_a) - 1] = ui[0]
                                        else:
                                            peaks_a.append(ui[0])
                                            ui = []
                                peaks_a.append((scaled_a[i], lst2_t[i]))
                        else:
                            peaks_a.append((scaled_a[i], lst2_t[i]))
    # Display local peaks
    print("Local peaks:", peaks_a)
    # Find local peaks
    peaks_f = []
    ui = []
    for i in range(1, len(scaled_f) - 1):
        if lst1_t[i] > lst1_t[0] + 3:
            if scaled_f[i] > scaled_f[i - 1] and scaled_f[i] >= scaled_f[i + 1]:
                if scaled_f[i] > 0.3:
                    if len(peaks_f) > 0:
                        if abs(peaks_f[len(peaks_f) - 1][1] - lst1_t[i]) < 2:
                            ui.append((scaled_f[i], lst1_t[i]))
                            # print(ui)
                        if abs(peaks_f[len(peaks_f) - 1][1] - lst1_t[i]) > 2:
                            if len(ui) > 0:
                                if ui[0] in peaks_f:
                                    pass
                                else:
                                    if len(peaks_f) > 0:
                                        peaks_f[len(peaks_f) - 1] = ui[0]
                                    else:
                                        peaks_f.append(ui[0])
                                        ui = []
                            peaks_f.append((scaled_f[i], lst1_t[i]))
                    else:
                        peaks_f.append((scaled_f[i], lst1_t[i]))
    # Display local peaks
    print("Local peaks:", peaks_f)

    print("peak_f", len(peaks_f), '\n',"peak_a", len(peaks_a))
    diff = []
    y = 0
    while y < min(len(peaks_a),len(peaks_f)):

        if abs(peaks_a[y][1] - peaks_f[y][1]) < 50:
            diff.append(abs(peaks_a[y][1] - peaks_f[y][1]))
            y += 1

        elif abs(peaks_a[y][1] - peaks_f[y][1]) < 50:

            diff.append(abs(peaks_a[y][1] - peaks_f[y][1]))
            y += 1
        elif abs(peaks_a[y][1] - peaks_f[y][1]) > 50:
            if len(diff) > 5:
                break
            else : pass
        else:
            pass
    print(diff)

    p = 0
    c=0
    for _ in range(len(diff)):
        if diff[_] < 2:
            p += diff[_]
            c+=1
    print(p / c)
    x = [x for x in range(len(diff))]
    # # Plot the graph
    fig1=plt.figure()
    ax1=fig1.add_subplot(111)
    ax1.bar(x, diff, color='blue',
            width=0.4)
    ax1.plot(x, diff, color='green')

    fig1.show()
    plt.show()
# latency(f_31_1=f_1,a_31_1=a_1)