import csv
from pathlib import Path
def check_csv(path):
    csv_lines = []
    with open(path, 'r') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            csv_lines.append(line)
    return csv_lines
