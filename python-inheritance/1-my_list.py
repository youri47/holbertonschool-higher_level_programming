#!/usr/bin/python3
"""Module contenant la classe MyList"""


class MyList(list):
    """Classe qui hérite de list avec une méthode pour afficher trié"""

    def print_sorted(self):
        """Affiche la liste triée en ordre croissant"""
        print(sorted(self))
