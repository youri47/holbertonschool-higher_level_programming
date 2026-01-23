#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Imprime les x premiers entiers d'une liste."""
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass  # On ignore les non-entiers
        except IndexError:
            raise  # On laisse remonter l'erreur d'index

    print()
    return count
