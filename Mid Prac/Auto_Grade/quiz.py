from csv import reader as read
from sys import argv


class Quiz:
    def __init__(self, path):
        with open(f'{path}', 'r') as file:
            data = [line for line in read(file)]
        self.data = data

    def get_question(self, number):
        if not isinstance(number, int):
            return None
        elif number <= 0 or len(self.data) < number:
            return None
        return self.data[number-1][0]

    def get_answer(self, number):
        if not isinstance(number, int):
            return None
        elif number <= 0 or len(self.data) < number:
            return None
        return int(self.data[number-1][-1])

    def grade(self, path):
        with open(f'{path}', 'r') as file:
            student = [line for line in read(file)]
        student = [answer[0] for answer in student]
        if len(self.data) != len(student):
            raise RuntimeError
        grade_dict = {'score': 0, 'wrong': []}
        for answer_index, answer in enumerate(student):
            if self.get_answer(answer_index+1) == int(answer):
                grade_dict['score'] += 1
            else:
                grade_dict['wrong'].append(self.get_question(answer_index+1))
        return grade_dict

    def get_full_question(self, value):
        if not isinstance(value, int):
            return None
        elif value <= 0 or len(self.data) < value:
            return None
        data = self.data[value-1]
        string = f'{data[0]}\n'
        for index, item in enumerate(data[1:5]):
            string += f'{int(index)+1} {item}\n'
        return string.rstrip()


def main():
    test = Quiz(argv[-1]).get_full_question(4)
    print(test)
    print(test.split('\n'))


if __name__ == '__main__':
    main()
