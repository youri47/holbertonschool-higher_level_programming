#!/usr/bin/python3
def safe_print_integer(value):
    """Imprime un entier avec "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
