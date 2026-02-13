#!/usr/bin/python3
"""Module qui retourne la description d'un objet pour la sérialisation JSON"""


def class_to_json(obj):
    """Retourne le dictionnaire description d'un objet pour la sérialisation JSON"""
    return obj.__dict__
