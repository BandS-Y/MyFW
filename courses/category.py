from abc import ABC


class AbstractCategory(ABC):

    def create_category(self):
        pass


class CategoryCourse(AbstractCategory):

    def __init__(self, name):
        self.name = name
        print(f'создана категория {name}')

    @classmethod
    def print_instances(cls):
        for instance in cls.instances:
            print(instance.name)

    def create_category(self):
        return self
