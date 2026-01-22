#!/usr/bin/python3
"""Module qui contient la fonction print_sorted_dictionary"""


def print_sorted_dictionary(a_dictionary):
    """Affiche un dictionnaire trié par clés"""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
