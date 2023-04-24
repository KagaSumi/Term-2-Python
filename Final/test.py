class Example:
    def __len__(self):
        return len(self.data)
def test_example():
    instance = Example()
    instance.data = [1,2,3]
    return len(instance) == 3
test_example()