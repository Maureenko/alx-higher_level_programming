#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""
import sys

# Importing the functions from the previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load the list from the JSON file, or create an empty list if it doesn't exist
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Append command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
