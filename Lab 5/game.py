from question_library import QuestionLibrary


class Game:
    """This class will be used to host the trivia game, this will require a .json file that contains the questions.
    Optionally you can specify the difficulty level of the question, the category of the questions, and the amount of questions you will 
    have to answer.
    """

    def __init__(self, filename: str = 'trivia.json', category: str = None, difficulty: str = None, number: int = None):
        """Creates a instance of the Trivia Game

        Args:
            filename (str, optional): Path to the json file containing the questions. Defaults to 'trivia.json'.
            category (str, optional): Category of question for the game. Defaults to None.
            difficulty (str, optional): Difficulty of the question for the game. Defaults to None.
            number (int, optional): Amount of questions for the game. Defaults to None.
        """
        self.question_library = QuestionLibrary(filename)
        self.questions = self.question_library.get_questions(
            category=category, difficulty=difficulty, number=number)
        self.score = 0

    def play(self) -> None:
        """Lets users play the game instance.
        """
        valid_input = ['1', '2', '3', '4']
        score_multi = {'easy': 1, 'medium': 2, 'hard': 3}
        for question in self.questions:
            print(question)
            user_input = input('Please enter your answer: ')
            while user_input not in valid_input:
                user_input = input('Please enter your answer: ')
            if str(question.answer_id) == user_input:
                self.score += 1 * score_multi[question.difficulty]
                print(f'Good Job! Score: {self.score}')
