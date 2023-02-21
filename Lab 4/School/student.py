class Student:
    def __init__(self, name: str, stu_id: str, grades: list):
        self.name = name
        self.stu_id = stu_id
        self.grades = grades

    @property
    def average(self) -> float:
        """Calculates the average grade for the student

        Returns:
            float: Returns the average grade
        """
        return round(sum(self.grades)/len(self.grades), 1)

    def __repr__(self) -> str:
        return f'{self.name:<20}| {self.stu_id:<9}|{self.average:^6}'


def main():
    # Creates test student
    test_student = Student('Matthew Mendoza', 'A7971499', [
                           56, 64, 94, 88, 60, 30, 94, 76, 89, 82])
    # Ensures that average grade works
    print(test_student.average)
    print(test_student)


if __name__ == "__main__":
    main()
