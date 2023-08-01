import matplotlib.pyplot as plt
import pandas as pd



def calculation(a, b):
    """
      Detects peaks in the input data and returns a list of tuples containing peak values and corresponding b-values.

      Parameters:
          a (list): List of numeric values representing data.
          b (list): List of numeric values representing data.

      Returns:
          list: A list of tuples with peak values from 'a' and corresponding values from 'b'.
      """
    peak = []
    for i in range(len(a)):
        if b[i] > b[0] + 2:
            if a[i] > 0.2:
                if len(peak) > 0:
                    if abs(peak[len(peak) - 1][1] - b[i]) > 3:
                        peak.append((a[i], b[i]))
                else:
                    peak.append((a[i], b[i]))
    return peak
def calculation_a(a, b):
    peak = []
    for i in range(len(a)):
        if b[i] > b[0] + 2:
            if a[i] > 0.15:
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
    min1=min(len(peaks_a), len(peaks_f))
    while y < min1:

        if y + 1<len(peaks_a) and abs(peaks_a[y][1] - peaks_f[y][1]) > 2:
            if abs(peaks_a[y + 1][1] - peaks_f[y][1]) < 2:
                diff.append(abs(peaks_a[y + 1][1] - peaks_f[y][1]))
                scaled_a.append(peaks_a[y + 1][0])
                scaled_f.append(peaks_f[y][0])
                lst1_t.append(peaks_f[y][1])
                lst2_t.append(peaks_a[y + 1][1])
                y += 1
            elif y + 1< len(peaks_f) and abs(peaks_a[y][1] - peaks_f[y + 1][1]) < 2:
                diff.append(abs(peaks_a[y][1] - peaks_f[y + 1][1]))
                scaled_a.append(peaks_a[y][0])
                scaled_f.append(peaks_f[y + 1][0])
                lst1_t.append(peaks_f[y + 1][1])
                lst2_t.append(peaks_a[y][1])
                y += 1
        elif abs(peaks_a[y][1] - peaks_f[y][1]) <= 2:
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
    c = [0.035]*max(len(peaks_a),len(peaks_f))
    d = [0.065]*max(len(peaks_a),len(peaks_f))
    e = [0.100]*max(len(peaks_a),len(peaks_f))
    plt.plot(x, c, color ='red')
    plt.plot(x,d,color='black')
    plt.fill_between(x,c,d, color="lightgray", label="Best range")
    plt.plot(x,e,color='green')
    plt.fill_between(x,d,e, color='pink', label="Average range")
    plt.bar(x, diff, color='blue',
            width=0.4)
    plt.plot(x, diff, color='orange',label ='latency')
    plt.legend()
    plt.title("Latency Graph")
    plt.xlabel("Number of iterations")
    plt.ylabel("Time (in Seconds)")
    plt.show()
