from sys import argv
import json
import os


def load_data(filepath):
    filepath = argv[1]
    if not os.path.exists(filepath):
    	return None
    with open(filepath, 'r') as file_handler:
    	return json.load(file_handler) 


def pretty_print_json(data):
    return print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data(filepath))