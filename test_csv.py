import os, csv, sys

class CsvReader:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        # print(file_path)
        self.output = []
        with open(self.file_path) as csv_file:
            reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in reader:
                self.output.append(', '.join(row))

    def print(self):
        
        for line in self.output:
            print(line)



def main():
    csv_reader = CsvReader(sys.argv[1])
    csv_reader.print()


if __name__ == "__main__":
    main()