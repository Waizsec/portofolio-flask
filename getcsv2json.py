import csv
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'static', 'assets', 'datapribadi.csv')


def showdata():
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]

    json_data = json.dumps(data)
    return json_data
