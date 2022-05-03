import sys
import openpyxl
import csv

def convert_xslx_to_csv(file_name):
    xslx_file = openpyxl.load_workbook(file_name)
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
                cell = cell.replace('\n', ' ')
                write_string += cell + ','
            write_string = write_string[:-1]
            write_string += '\n'
            csv_file.write(write_string)

def read_csv_file(file_name):
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        # for row in reader:


def main():
    xlsx_file = sys.argv[1]
    convert_xslx_to_csv(xlsx_file)
    read_csv_file(xlsx_file)

if __name__ == "__main__":
    main()