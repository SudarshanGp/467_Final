import csv

def parse_file(file_path):
    print file_path
    with open(file_path,"rb") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            print row