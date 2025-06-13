def count_vowels(word: str) -> int:
    """
    Counts the number of vowels in a given word.

    Args:
        word (str): The input string to count vowels from. The string
            can include alphabetic characters in any case.

    Returns:
        int: The number of vowels found in the input string.
    """
    vowels = set("aeiouyéèêëàâäùûüôöîïœ")
    no_duplicate_vowels = set(letter for letter in word.lower() if letter in vowels)
    # return sum(1 for letter in word.lower() if letter in vowels)
    return len(no_duplicate_vowels)


def create_list(words: list[str]) -> list[tuple[str, int]]:
    """
    Creates a list of tuples where each tuple contains a word and its corresponding vowels count.

    Args:
        words (list[str]): A list of strings from which tuples will be created.

    Returns:
        list[tuple[str, int]]: A list of tuples, where each tuple contains a string and
        its corresponding vowels count.
    """
    return [(word, count_vowels(word)) for word in words]


if __name__ == "__main__":
    words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
    comprehension_list = create_list(words)
    print(comprehension_list)
