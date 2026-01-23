#!/usr/bin/python3
"""
Module de tests unitaires pour max_integer.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests pour la fonction max_integer."""

    def test_ordered_list(self):
        """Test avec une liste ordonnée."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test avec une liste non ordonnée."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test avec le max au début."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test avec le max au milieu."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test avec un seul élément."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test avec une liste vide."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test avec des nombres négatifs."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test avec des nombres positifs et négatifs."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_floats(self):
        """Test avec des floats."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_int_float(self):
        """Test avec int et float mélangés."""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_string(self):
        """Test avec une string."""
        self.assertEqual(max_integer("abcd"), 'd')

    def test_list_of_strings(self):
        """Test avec une liste de strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_empty_string(self):
        """Test avec une string vide."""
        self.assertIsNone(max_integer(""))

    def test_none(self):
        """Test sans argument (utilise la valeur par défaut)."""
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()
