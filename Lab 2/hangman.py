"""
ACIT2515 Lab

Week 2 -- complete this file!

"""
# The number of turns allowed is a global constant
NB_TURNS = 10
from string import ascii_letters
from random import randint
def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    # WRITE YOUR CODE HERE !
    with open("words.txt", "r") as f:
        word_list = [element.rstrip() for element in f.readlines()]
        num = randint(0,len(word_list)-1)
    return word_list[num].upper()

def show_letters_in_word(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    # WRITE YOUR CODE HERE
    my_string = ''
    for char in word:
        if char.upper() in letters or char.lower() in letters:
            my_string += char.upper() + ' '
        else:
            my_string += '_ '
    return my_string.rstrip()

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    for character in word:
        if character not in letters:
            return False
    return True

def verify_input(string:str, Guessed:list[str]) -> bool:
    """This function takes in the user input and the guessed letters and returns a boolean indicating if the current input is a valid input


    Args:
        string (str): This is the user input
        Guessed (list[str]): The Current list of guessed letters in a list

    Returns:
        bool: This boolean will return False if the input is not a valid input and True if the input is valid.
    """    
    if len(string) != 1:
        print("Please enter only one Letter.")
        return False
    elif string not in ascii_letters:
        print("Please enter a Letter.")
        return False
    elif string in Guessed:
        print("You have already tried this letter.")
        return False
    return True

def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    # WRITE YOUR CODE HERE
    Current_Turn = 0
    Word = pick_random_word()
    Guessed_Letters = []
    print(show_letters_in_word(Word, Guessed_Letters))
    while (Current_Turn != turns):
        user_input = input('Please enter a letter: ').upper()
        while not verify_input(user_input,Guessed_Letters):
            user_input = input('Please try again: ').upper()
        Guessed_Letters.append(user_input)
        print(show_letters_in_word(Word, Guessed_Letters))
        Current_Turn += 1
        if all_letters_found(Word, Guessed_Letters):
            print("Good Job! You won!")
            break
    if Current_Turn == turns:
        print(f"Sorry you lost the word was {Word}")
    pass

if __name__ == "__main__":
    main(NB_TURNS)