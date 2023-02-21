import random


class Question:
    """This the question class, which holds the frame work of a question. 
    It requires a question, the correct answer, incorrect answer,category, and difficulty of the question.
    """

    def __init__(self, question: str, correct_answer: str, incorrect_answer: list[str], category: str, difficulty: str):
        """This creates a instance of a Question

        Args:
            question (str): This represents the question that is being asked.
            correct_answer (str): This represents the answer to the question
            incorrect_answer (list[str]): This is the incorrect answer to the question
            category (str): This is the category the question falls under
            difficulty (str): The difficulty of the question should be easy,medium or hard

        Raises:
            AttributeError: If the difficulty is not easy,medium or hard this error is raised

        Note: answer_id is incremented by 1 so that the id will match the enumerated value
        """
        if difficulty.lower() not in ['easy', 'medium', 'hard']:
            raise AttributeError(
                "Difficulty must be one of 'easy','medium','hard.")
        self.difficulty = difficulty.lower()
        self.answers = incorrect_answer + [correct_answer]
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) + 1
        self.question = question
        self.category = category

    def __str__(self) -> str:
        string = f'{self.question}\n'
        for number, answer in enumerate(self.answers):
            string += f'{number+1} {answer}\n'
        return string.rstrip()


def main():
    """This a test function that I used while creating this module
    """
    test_question = Question("What is the name of the instructor?", "Tim",
                             ["Alice", "Bob", "John"], 'test', 'easy')
    print(str(test_question))


if __name__ == '__main__':
    main()
