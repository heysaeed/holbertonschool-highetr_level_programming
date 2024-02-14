#!/usr/bin/python3
"""Add items to a list stored in a JSON file.

This script appends command-line arguments to a list stored in 'add_item.json'.
If the file does not exist, it creates a new list. It uses external functions
for loading from and saving to JSON files.

Usage:
    ./script_name arg1 arg2 ...
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"


if __name__ == "__main__":
    try:
        json_file = load_from_json_file(file_name)
    except FileNotFoundError:
        json_file = []
json_file.extend(sys.argv[1:])
save_to_json_file(json_file, file_name)
