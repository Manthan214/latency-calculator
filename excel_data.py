import xlsxwriter

def Starting_workbook():
    """
        Creates and returns a new XLSX workbook file named 'data_output.xlsx',
        with a new worksheet and a header format.

        Returns:
            A tuple containing the XlsxWriter Workbook object, the worksheet object,
            and the header format object.
        """
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
    """
    Takes a dictionary `x` as input and returns a list of values sorted in a specific order.

    Args:
    x (dict): A dictionary containing the following keys: Listen_start, Video_play, flash detection, Video_pause,
              Listen_stop, start_diff.

    Returns:
    list: A list of values sorted in the following order: Listen_start, flash detection, Video_play, Video_pause,
          Listen_stop, start_diff.
    """
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
    """
        Creates a new table in the specified worksheet with given data and header format. It also adds a calculated column to
        the table based on a formula.

        :param ws: The worksheet to add the table to.
        :type ws: xlsxwriter.worksheet.Worksheet
        :param data1: The data to be added to the table.
        :type data1: list[list]
        :param header_format: The format to be used for the table header.
        :type header_format: xlsxwriter.format.Format
        """
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
    """ Closes the workbook """
    wb.close()

