class Person:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise AttributeError('name must be a string')
        elif name.isdigit():
            raise AttributeError('name must be a string')
        elif len(name) < 3:
            raise AttributeError('name must be at least 3 characters long')
        if not isinstance(int(age), int) or int(age) < 0:
            raise AttributeError('Age must be an positive integer')
        self.name = name
        self.age = int(age)

    def get_name(self):
        return f'{self.name.upper()} / {self.age}'
