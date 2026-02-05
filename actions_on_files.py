import csv
from pathlib import Path
def read_csv(path):
    csv_lines = []
    with open(path, 'r') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            csv_lines.append(line)
    return csv_lines

def return_budget_amount(path):
    try:
        with open(path, "r") as f:
            str_amount = f.read()
            return float(str_amount)
    except Exception as e:
        print(f"error! type error:{e}")

def read_airports_file(path):
        airports_list = []      
        with open(path, 'r') as f:
            airports = csv.DictReader(f)
            for row in airports:
                airports_list.append(dict(row))
        return airports_list