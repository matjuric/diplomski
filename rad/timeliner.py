# pokrece se sa
# python timeliner.py ../../../Podaci/ScenarioReview.xlsx
# napravi ljepsi poziv skripte


from cProfile import label
import sys
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

def convert_xslx_to_csv(xlsx_file, csv_file):
    xslx_file = openpyxl.load_workbook(xlsx_file)
    sheet = xslx_file.active
    data = sheet.rows

    with open('tmp.csv', 'w+') as csv_file:
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

    # ako bude nekada trebalo, moze se na neki nacin citati xlsx na pandasom, ali to mi radi bas kako zelim
    # problem je sa \n u nekim cellovima, potrga se na tome
    # df = pd.read_excel(xlsx_file, engine='openpyxl')
    # print(df)
    # # df.to_csv(csv_file)#, sep='\n')
    # # df.replace(r'\n', ' ', regex=True)
    # # df.to_csv(csv_file)

def read_csv_file(csv_file):
    df = pd.read_csv(csv_file)
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
    starting_times = df['Beginning'][:5]
    # print(starting_times[0]); exit()
    # print(date.fromtimestamp(starting_times[1])); exit()

    # print(starting_times)
    labels = df['Name / Sender'][:5]
    texts = df['Parameters / Text Message']
    labels = ['{0}\n{1}'.format(d, l) for l,d in zip(labels, texts)]

    labels = ['{0}\n{1}'.format(d, l) for l,d in zip(labels, starting_times)]

    # print(labels); exit()
    
    fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
    _ = ax.set_ylim(-2, 1.75)
    # _ = ax.set_xlim(date(2022, 3, 10), date(2022, 5, 5))
    _ = ax.axhline(0, xmin=0.05, xmax=0.95, c='deeppink', zorder=1)
    _ = ax.scatter(starting_times, np.zeros(len(starting_times)), s=120, c='palevioletred', zorder=2)
    _ = ax.scatter(starting_times, np.zeros(len(starting_times)), s=30, c='darkmagenta', zorder=3)

    label_offsets = np.zeros(len(starting_times))
    label_offsets[::2] = 0.35
    label_offsets[1::2] = -0.7
    for i, (l, d) in enumerate(zip(labels, starting_times)):
        _ = ax.text(d, label_offsets[i], l, ha='center', fontfamily='serif', fontweight='bold', color='royalblue',fontsize=12)

    stems = np.zeros(len(starting_times))
    stems[::2] = 0.3
    stems[1::2] = -0.3
    markerline, stemline, baseline = ax.stem(starting_times, stems, use_line_collection=True)
    _ = plt.setp(markerline, marker=',', color='darkmagenta')
    _ = plt.setp(stemline, color='darkmagenta')


    for spine in ["left", "top", "right", "bottom"]:
        _ = ax.spines[spine].set_visible(False)
    
    _ = ax.set_xticks([])
    _ = ax.set_yticks([])
    
    _ = ax.set_title('Test timeline', fontweight="bold", fontfamily='serif', fontsize=16, 
                    color='royalblue')


    plt.show()
    # df = pd.read_csv(csv_file)
    # cols = df.head()
    # print(cols)


def main():
    xlsx_file = sys.argv[1]
    csv_file = sys.argv[2]
    convert_xslx_to_csv(xlsx_file, csv_file)
    read_csv_file(csv_file)

if __name__ == "__main__":
    main()