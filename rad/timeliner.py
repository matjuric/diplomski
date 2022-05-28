# pokrece se sa
# python timeliner.py ScenarioReview.xlsx test.csv

import sys
from tracemalloc import start
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from datetime import date, datetime
import numpy as np

def convert_xslx_to_csv(xlsx_file, csv_file):
    xslx_file = openpyxl.load_workbook(xlsx_file)
    sheet = xslx_file.active
    data = sheet.rows

    with open(csv_file, 'w+') as csv_file:
        for row in data:
            l = list(row)
            write_arr = []
            for i in range(len(l)):
                write_arr.append(str(l[i].value))
            
            write_string = ""
            for cell in write_arr:
                # makni '\n' u cellovima
                # makni ',' u cellovima
                cell = cell.replace('\n', ' ')
                cell = cell.replace(',', ' ')
                write_string += cell + ','
            write_string = write_string[:-1]
            write_string += '\n'
            csv_file.write(write_string)

def read_csv_file(csv_file):
    parse_dates = ['Beginning']
    df = pd.read_csv(csv_file, parse_dates=parse_dates)
    column_names = [
        'Type',
        'Beginning',
        'Name / Sender',
        'Ending / Title',
        'Initiator / Receiver'
        'Parameters / Text Message',
        'Content'
    ]
    
    # events
    starting_times = pd.to_datetime(df['Beginning']).apply(lambda x: x.replace(microsecond=0))
    labels = df['Name / Sender']
    texts = df['Parameters / Text Message']
    labels = ['{0}\n{1}'.format(d, l) for l,d in zip(labels, texts)]

    labels = ['{0}\n{1}'.format(d, l) for l,d in zip(labels, starting_times)]
    
    fig, ax = plt.subplots(figsize=(12, 6), constrained_layout=True)

    levels = np.tile([-2.5, 2.5, -1, 1, -0.5, 0.5],
                 int(np.ceil(len(starting_times)/6)))[:len(starting_times)]

    ax.vlines(starting_times, 0, levels, color="tab:red")
    ax.plot(starting_times, np.zeros_like(starting_times), "-o",
        color="k", markerfacecolor="w")

    for d, l, r in zip(starting_times, levels, labels):
        ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")



    for spine in ["left", "top", "right", "bottom"]:
        _ = ax.spines[spine].set_visible(False)
    
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)

    # plt.show()
    plt.savefig('test.png')


def main():
    xlsx_file = sys.argv[1]
    csv_file = sys.argv[2]
    convert_xslx_to_csv(xlsx_file, csv_file)
    read_csv_file(csv_file)

if __name__ == "__main__":
    main()