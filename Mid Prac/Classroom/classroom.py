class Classroom:
    def __init__(self, room, inst_name):
        self.room = room
        self.instructor = inst_name
        self.students = list()

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return f'Room {self.room} [{self.instructor}] - {len(self.students)} students'

    def __add__(self, other):
        self.students.append(other)

    def add_student(self, student):
        self.students.append(student)
