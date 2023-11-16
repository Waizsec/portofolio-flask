import csv
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'static', 'assets', 'datapribadi.csv')


def csv_to_json(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]

    json_data = json.dumps(data)
    return json_data


def showdata():
    if os.path.exists(csv_file_path):
        json_data = csv_to_json(csv_file_path)
        return json_data
    else:
        return 'CSV file not found.'
