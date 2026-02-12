#!/usr/bin/python3
"""Module qui sauvegarde un objet dans un fichier JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Écrit un objet dans un fichier texte en utilisant une représentation JSON"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
