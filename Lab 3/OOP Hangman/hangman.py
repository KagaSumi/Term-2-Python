from random import randint
from string import ascii_letters

class SecretWord:
    def __init__(self, word=None):
        self.word = word
        if self.word == None:
            with open("words.txt", "r") as f:
                word_list = [element.rstrip() for element in f.readlines()]
                num = randint(0, len(word_list)-1)
            self.word = word_list[num].upper()

    def show_letters(self, Guessed: list) -> str:
        """This function returns a string in the representation of "_ _ _ _" with any characters guessed properly filled in

        Args:
            Guessed (list): List of guessed letters

        Returns:
            str: String in the representation of "_ _ _ _" with any characters guessed properly filled In
        """
        my_string = ''
        for char in self.word.upper():
            if char in Guessed or char.lower() in Guessed:
                my_string += char.upper() + ' '
            else:
                my_string += '_ '
        return my_string.rstrip()

    def check_letters(self, Guessed: list) -> bool:
        """Function to check if player has guessed entire all the letters of the secret word

        Args:
            Guessed (list): list of guessed letter

        Returns:
            bool: True if player has guessed all letters false if not
        """
        for character in self.word:
            if character.upper() not in Guessed:
                if character.lower() not in Guessed:
                    return False
        return True

    def check(self, Guess: str) -> bool:
        """Function checks if player guessed the entire word correctly

        Args:
            Guess (str): Player Guess

        Returns:
            bool: True if they have guessed correctly, False if incorrect
        """
        return self.word.upper() == Guess.upper()


class Game:
    def __init__(self, turns=10):
        self.turns = turns
        self.Word = SecretWord()
        self.Guessed = []

    def play_one_round(self) -> bool:
        """Plays one round of the game and returns if the player has guessed the word correctly

        Returns:
            bool: True if player wins, False otherwise
        """
        Guessing = True
        while Guessing:
            Guessing = False
            user_input = input('Please Guess a Letter/Word: ')
            if not user_input:
                print('Please enter an input')
                Guessing = True
            elif user_input.lower() in self.Guessed or user_input.upper() in self.Guessed:
                print('You have already guessed this letter:')
                Guessing = True
            elif len(user_input) == 1 and user_input not in ascii_letters:
                print("This isn't a valid input")
                Guessing = True
        self.turns -= 1
        if len(user_input) == 1:
            self.Guessed.append(user_input)
            print(self.Word.show_letters(self.Guessed))
            return self.Word.check_letters(self.Guessed)
        else:
            return self.Word.check(user_input)

    def play(self) -> bool:
        """This is the play method, which starts the game and

        Returns:
            bool: Returns True if the if they win, False if they lose
        """
        print(self.Word.show_letters(self.Guessed))
        while self.turns != 0:
            if self.play_one_round():
                print('Good job you won!')
                return True
        print(f'Looks like you lost the word was {self.Word.word}')
        return False


def main():
    My_Game = Game()
    My_Game.play()


if __name__ == '__main__':
    main()

