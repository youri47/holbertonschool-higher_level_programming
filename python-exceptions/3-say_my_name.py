#!/usr/bin/python3
"""
Module pour afficher un nom complet.
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche My name is <first_name> <last_name>.

    Args:
        first_name: prénom (string)
        last_name: nom de famille (string), défaut = ""

    Raises:
        TypeError: si first_name ou last_name n'est pas une string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
