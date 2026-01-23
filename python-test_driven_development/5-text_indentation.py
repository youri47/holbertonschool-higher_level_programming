#!/usr/bin/python3
"""
Module pour l'indentation de texte.
"""


def text_indentation(text):
    """
    Affiche un texte avec 2 nouvelles lignes après chaque '.', '?' et ':'.

    Args:
        text: le texte à formater

    Raises:
        TypeError: si text n'est pas une string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    lines = result.split("\n")
    for idx, line in enumerate(lines):
        if idx == len(lines) - 1:
            print(line.strip(), end="")
        else:
            print(line.strip())
