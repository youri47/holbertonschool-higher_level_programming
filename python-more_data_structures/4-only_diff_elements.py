#!/usr/bin/python3
"""Module qui contient la fonction only_diff_elements"""


def only_diff_elements(set_1, set_2):
    """Retourne un set des éléments présents dans un seul des deux sets"""
    return set_1 ^ set_2
