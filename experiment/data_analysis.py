import matplotlib.pyplot as plt
import pandas as pd

def data_analy(f_31_1, a_31_1):
    """Perform data analysis and generate visualizations.

    This function takes in two lists of data, `f_31_1` and `a_31_1`, performs data analysis, and generates visualizations using matplotlib and pandas.

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

    for j in a_31_1:
        if j:
            lst2_v.append(j[0])
            lst2_t.append(j[1])
            threshold_a.append(0.25)
    print(len(lst2_v), "audio")

    max_v_a = max(lst2_v)
    max_v_f = max(lst1_v)
    scaled_f = []
    scaled_a = []
    for _ in lst1_v:
        scaled_f.append(_ / max_v_f)
    for _ in lst2_v:
        scaled_a.append(_ / max_v_a)

    min_time = min(lst1_t[0], lst2_t[0])
    max_time = max(max(lst1_t), max(lst2_t))
    print("min_time", min_time)
    print("max_time", max_time)
    a = max(len(lst2_t), len(lst1_t))
    print("diff", round((max_time - min_time) / 5))
    print(a)

    flash_data = {'flash value': scaled_f, 'flash_time': lst1_t}
    audio_data = {'Audio value': scaled_a, 'Audio_time': lst2_t}
    fdata = pd.DataFrame(flash_data)
    adata = pd.DataFrame(audio_data)
    writer = pd.ExcelWriter('analysis_31.xlsx', engine='xlsxwriter')
    fdata.to_excel(writer, sheet_name='Sheet1', index=False)
    adata.to_excel(writer, sheet_name='Sheet2', index=False)
    writer.close()
    df = pd.read_excel('analysis_31.xlsx', sheet_name='Sheet1')
    da = pd.read_excel('analysis_31.xlsx', sheet_name='Sheet2')
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.plot(da['Audio_time'], da['Audio value'], label="audio")
    ax2.plot(df['flash_time'], df['flash value'], label="flash")
    # plt.plot(df['flash_time'], threshold_f, label="Threshold flash")
    #
    # plt.plot(da['Audio_time'], threshold_a, label="Threshold audio")
    # plt.bar(da['Audio_time'], da['Audio value'], label="audio",color="black",width=0.4)
    #
    # plt.bar(df['flash_time'], df['flash value'], label="flash",color="red",width=0.4)
    fig2.show()
    plt.show()
# data_analy(f_1,a_1)
