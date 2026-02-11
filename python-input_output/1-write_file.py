#!/usr/bin/python3
"""Module qui écrit dans un fichier texte"""


def write_file(filename="", text=""):
    """Écrit une string dans un fichier UTF-8 et retourne le nombre de caractères écrits"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
