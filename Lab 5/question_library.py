from json import load
import random

from question import Question


class QuestionLibrary:
    """This is a class that will be used to generate a question bank for our trivia game.
    Functions
            Find questions that match specific criteria with get_questions() function
            Find all unique categories for the questions bank with get_categories() function
    """

    def __init__(self, filename='trivia.json'):
        """Creates a list of question object using a .json file

        Args:
            filename (str, optional): Path to a json file. Defaults to 'trivia.json'.
        """
        with open(f'{filename}', 'r') as fp:
            content = load(fp)
        self.questions = []
        for item in content:
            question = Question(
                question=item['question'],
                correct_answer=item['correct_answer'],
                incorrect_answer=item['incorrect_answers'],
                category=item['category'],
                difficulty=item['difficulty']
            )
            self.questions.append(question)

    def __len__(self):
        return len(self.questions)

    def get_categories(self) -> list[str]:
        """Returns a list of unique categories

        Returns:
            list[str]: List of unique categories from the entire Question Library
        """
        return list(set(question.category for question in self.questions))

    def get_questions(self, number: int = None, category: str = None, difficulty: str = None) -> list[Question]:
        """This function returns a list of Question objects relating to the given criteria passed through. If there is no number provided then it will
        return all Question objects that match the given criteria.

        Args:
            number (int, optional): This is the amount of question returned in the list. Defaults to None.
            category (str, optional): This is the category of question, if declared all question will fall under the category. Defaults to None.
            difficulty (str, optional): This is the difficulty of the questions, if declared all question will be the declared difficulty. Defaults to None.

        Returns:
            list[Question]: A list of Question that match the criteria
        """
        filter_question = self.questions.copy()
        random.shuffle(self.questions)
        if difficulty not in ['easy', 'medium', 'hard']:
            difficulty = None
        if category not in self.get_categories():
            category = None
        if difficulty:
            filter_question = list(filter(
                lambda question: question.difficulty == difficulty, filter_question))
        if category:
            filter_question = list(filter(
                lambda question: question.category == category, filter_question))
        if number:
            return filter_question[:number]
        return filter_question


def main():
    """This a test function that I used while creating this module
    """
    test_question_library = QuestionLibrary()
    print(len(test_question_library))
    print(test_question_library.questions)


if __name__ == '__main__':
    main()
