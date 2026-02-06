#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite - on ne peut PAS l'instancier directement."""

    @abstractmethod
    def sound(self):
        """Chaque animal DOIT définir son propre son."""
        pass


class Dog(Animal):
    """Hérite de Animal, donc DOIT implémenter sound()."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Hérite de Animal, donc DOIT implémenter sound()."""

    def sound(self):
        return "Meow"
