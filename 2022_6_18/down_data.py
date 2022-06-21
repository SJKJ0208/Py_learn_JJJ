

def test1():
    import csv
    file_name = 'test.csv'
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)