#!/usr/bin/python3
"""Module qui contient la fonction simple_delete"""


def simple_delete(a_dictionary, key=""):
    """Supprime une clé du dictionnaire si elle existe"""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
