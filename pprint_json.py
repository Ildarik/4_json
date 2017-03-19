''' TODO
[x] 1 doc -> README.md
[x] 2 path
[x] 3 comments, why? What's this?
[ ] readme
[ ] cyrillic
'''

from sys import argv
import json
import os

# models.json in repo
# filepath = '/home/ildar/Projects/DevMan/4_json/models.json'
filepath = argv[1]


def load_data(filepath):
    if not os.path.exists(filepath):
    	return None
    with open(filepath, 'r') as file_handler:
    	return json.load(file_handler) 			# ? OR return data = json.load...


def pretty_print_json(data):
    return print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_data(filepath))