#!/usr/bin/python3
import sys

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"


if __name__ == "__main__":
    try:
        json_file = load_file(file_name)
    except FileNotFoundError:
        json_file = []
json_file.extend(sys.argv[1:])
save_file(json_file, file_name)