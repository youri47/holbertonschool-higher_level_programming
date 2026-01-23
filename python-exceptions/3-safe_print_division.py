#!/usr/bin/python3
def safe_print_division(a, b):
    """Divise a par b et affiche le résultat."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
