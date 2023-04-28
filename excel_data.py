import xlsxwriter

def Starting_workbook():
    wb = xlsxwriter.Workbook('data_output.xlsx')
    ws = wb.add_worksheet()
    header_format = wb.add_format({
        'bold': True,
        'bg_color': '#2F81BD',
        'border': 10,
        'align': 'center',
        'border_color': 'black'
    })
    return wb,ws,header_format
def appending(x):
    dsat = []
    for i, j in x.items():

        if i == 'Listen_start':
            dsat.insert(0, j)
        elif i == 'Video_play':
            dsat.insert(2, j)
        elif i == 'flash detection':
            dsat.insert(1, j)
        elif i == 'Video_pause':
            dsat.insert(3, j)
        elif i == 'Listen_stop':
            dsat.insert(4, j)
        elif i == 'start_diff':
            dsat.insert(5, None)
    print(dsat)
    return dsat
def creating_table(ws,data1,header_format):
    formula1 = '=(marklist1[@[Video_play]]-[@[Listen_start]])'
    ws.merge_range('A1:F1', 'Merged Cells')
    ws.write('A1', 'Table 1', header_format)
    tbl1 = ws.add_table("A2:F6",
                        {'data': data1,
                         'autofilter': False,
                         'name': 'marklist1',
                         'header_row': True,
                         'columns': [
                             {'header': 'Listen_start'},
                             {'header': 'flash detection'},
                             {'header': 'Video_play'},
                             {'header': 'Video_pause'},
                             {'header': 'Listen_stop'},
                             {'header': 'start_diff', 'formula': formula1}
                         ]
                         })

def close_workbook(wb):
    wb.close()

















# from testScripts import testVideo
# from audio import listen
# import pandas as pd
# dict_excel = {'Listen_start': [], 'Video_play': [], 'flash detection': [], 'Video_pause': [], 'Listen_stop': [],
#               'start_diff': []}
#
#
# def difference():
#     start_difference = float(testVideo.dict['Video_play']) - float(testVideo.dict['Listen_start'])
#     testVideo.dict["start_diff"] = start_difference
#
#     for j in dict_excel.keys():
#         dict_excel[j].extend([testVideo.dict[j]])
#
# def excel_disp():
#     df = pd.DataFrame(dict_excel)
#     df.to_excel("output_final.xlsx", index=False)
#     # stop_difference = testVideo.dict['Video_pause'] - testVideo.dict['Listen_stop']
#     # testVideo.dict["stop_diff"] = stop_difference

