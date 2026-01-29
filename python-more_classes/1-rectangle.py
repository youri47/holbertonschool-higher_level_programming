#!/usr/bin/python3
"""Module qui définit une classe Rectangle avec validation"""


class Rectangle:
    """Classe qui représente un rectangle avec largeur et hauteur"""

    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec largeur et hauteur
        
        Args:
            width (int): largeur du rectangle (défaut: 0)
            height (int): hauteur du rectangle (défaut: 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Récupère la largeur du rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur du rectangle avec validation
        
        Args:
            value (int): nouvelle largeur
            
        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Définit la hauteur du rectangle avec validation
        
        Args:
            value (int): nouvelle hauteur
            
        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est négatif
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
