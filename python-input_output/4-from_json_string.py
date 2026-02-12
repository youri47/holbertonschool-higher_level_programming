#!/usr/bin/python3
"""Module qui convertit une string JSON en objet Python"""
import json


def from_json_string(my_str):
    """Retourne un objet Python à partir d'une string JSON"""
    return json.loads(my_str)
