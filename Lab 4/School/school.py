from csv import reader

from student import Student


class School:
    def __init__(self):
        with open("students.csv", 'r') as student_csv:
            students = [line for line in reader(student_csv)]
        with open("grades.csv", 'r') as grade_csv:
            grades = [[line[0], map(int, line[1:])]
                      for line in reader(grade_csv)]
        for student in students:
            for grade in grades:
                if student[1] == grade[0]:
                    student.append(list(grade[1]))
        self.student_list = [
            Student(student[0], student[1], student[2]) for student in students[1:]]

    def find_students_by_name(self, name: str) -> list[Student]:
        """This Function returns a list of student objects with the matching name

        Raises:
            TypeError: Rases when the instance of name is not a string

        Returns:
            List[Str]: A list of Student Objects
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        return [student for student in self.student_list if name in student.name]

    def find_students_by_id(self, find_id: str,) -> list[Student]:
        """This function returns a list of student objects with the matching student id

        Args:
            find_id (str): string representing the student_id to search for

        Raises:
            TypeError: Raises when the id is not a string

        Returns:
            list[Student]: A list of Student Objects that match the student id
        """
        if not isinstance(find_id, str):
            raise TypeError("find_id must be a string")
        return [student for student in self.student_list if find_id in student.stu_id]

    def print_student_list(self, full=False, sort='name') -> None:
        """This function takes in 2 optional arguments and prints the list of students name,id,
        average and optionally the list of grades. When sorting the first column will change
        to the sort by field

        Args:
            full (bool, optional): Boolean to print all the grades. Defaults to False.
            sort (str, optional): Determines how the output is sorted by options are name, id,
            average. Defaults to 'name'.

        Raises:
            TypeError: Raises if sort isn't a string
            ValueError: Raises when sort isn't
        """
        if not isinstance(sort, str):
            raise TypeError("Sort must be a string")
        sort = sort.lower()
        if sort not in ['name', 'id', 'average']:
            raise ValueError('Sort must be one of "name" | "id" | "average"')
        name_dict = {}
        id_dict = {}
        average_dict = {}
        for index in range(len(self.student_list)-1):
            name_dict[self.student_list[index].name] = index
            id_dict[self.student_list[index].stu_id] = index
            average_dict[self.student_list[index].average] = index
        if sort == 'name':
            sorted_list = [name_dict[name]
                           for name in sorted(name_dict.keys())]
        elif sort == 'id':
            sorted_list = [id_dict[id] for id in sorted(id_dict.keys())]
        else:
            sorted_list = [average_dict[avg]
                           for avg in sorted(average_dict.keys(), reverse=True)]
        for value in sorted_list:
            if full:
                grade_string = ''
                for grade in self.student_list[value].grades:
                    grade_string += f'{grade:>x4} '
                grade_string.rstrip()
                print(
                    f'{self.student_list[value]}|{grade_string}')
            else:
                print(self.student_list[value])


def main():
    # Creates a test School
    test_school = School()
    # Testing finding
    print(test_school.find_students_by_id('A9737593'))
    print(test_school.find_students_by_name('John'))
    # Test all different type of prints
    # test_school.print_student_list()
    # test_school.print_student_list(False, 'id')
    test_school.print_student_list(False, 'AVeraGE')
    # test_school.print_student_list(True)
    # test_school.print_student_list(True, 'ID')
    # test_school.print_student_list(True, 'average')


if __name__ == "__main__":
    main()
