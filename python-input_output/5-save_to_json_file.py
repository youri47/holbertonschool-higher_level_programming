#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Serialize an object to JSON and save it to a text file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json_string = json.dumps(my_obj)
        f.write(json_string)
