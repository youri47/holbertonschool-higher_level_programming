#!/usr/bin/python3
"""Module qui contient la fonction search_replace"""


def search_replace(my_list, search, replace):
    """Remplace toutes les occurrences de search par replace dans une nouvelle liste"""
    return [replace if x == search else x for x in my_list]
