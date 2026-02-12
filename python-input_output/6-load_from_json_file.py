#!/usr/bin/python3
"""Module qui charge un objet depuis un fichier JSON"""
import json


def load_from_json_file(filename):
    """Crée un objet Python à partir d'un fichier JSON"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
