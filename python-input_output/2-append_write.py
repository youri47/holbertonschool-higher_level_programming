#!/usr/bin/python3
"""Module qui ajoute du texte à la fin d'un fichier"""


def append_write(filename="", text=""):
    """Ajoute une string à la fin d'un fichier UTF-8 et retourne le nombre de caractères ajoutés"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
