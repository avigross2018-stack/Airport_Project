import csv
from pathlib import Path
def check_csv(path):
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
