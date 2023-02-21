def scrabble_score(word: str) -> int:
    """Calculates how many Scrabble points a word is worth"""

    LETTER_SCORES = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10,
    }

    total = 0
    for letter in word:
        total += LETTER_SCORES[letter]
    return total


if __name__ == "__main__":
    word = input("Enter a word: ")
    score = scrabble_score(word)
    print(word, "is worth", score, "Scrabble points")
