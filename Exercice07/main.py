# Écrivez une fonction appelée square qui prend en paramètre un nombre et renvoie le carré de ce nombre.
#
# Cependant, la fonction doit gérer les erreurs potentielles, notamment le cas où le paramètre n'est pas un nombre (int ou float).
#
# Si le paramètre n'est pas un nombre, la fonction doit afficher un message d'erreur "Le paramètre doit être un nombre !" et renvoyer None.


def square(number_to_square: int | float) -> int | float:
    """
    Calculates the square of a given number.

    Args:
        number_to_square: The number to be squared.

    Returns:
        The square of the input number.

    Raises:
        ValueError: If the input is not of type int or float.
    """
    if not isinstance(number_to_square, (int, float)):
        raise ValueError("Parameter must be a number")
    return number_to_square**2


if __name__ == "__main__":
    try:
        # square = square(10)
        # square = square("a")
        # square = square(0)
        square = square()
        print("Square is :", square)
    except ValueError as error:
        print("An error happened:")
        print(error)
    except TypeError as error:
        print("An error happened:")
        print(error)
