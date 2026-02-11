#!/usr/bin/python3
"""Module qui lit un fichier texte"""


def read_file(filename=""):
    """Lit un fichier texte UTF-8 et l'affiche sur stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
