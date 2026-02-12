#!/usr/bin/python3
"""Module qui convertit un objet en string JSON"""
import json


def to_json_string(my_obj):
    """Retourne la représentation JSON (string) d'un objet"""
    return json.dumps(my_obj)
