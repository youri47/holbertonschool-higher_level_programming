#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""JSON file to store the list"""
filename = "add_item.json"

"""If the file doesn t exist, it should be created"""
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []


"""Command-line arguments (excluding script name)"""
args = sys.argv[1:]


"""Append new arguments to the list"""
my_list.extend(args)


"""Save updated list back to the JSON file"""
save_to_json_file(my_list, filename)
