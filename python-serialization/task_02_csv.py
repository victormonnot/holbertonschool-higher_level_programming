#!/usr/bin/python3
"""file"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV to JSON"""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except Exception:
        return False
