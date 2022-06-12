from abc import ABC


class AbstractCategory(ABC):

    def create_category(self):
        pass


class CategoryCourse(AbstractCategory):
    instances = []

    def __init__(self, name):
        self.name = name
        self.__class__.instances.append(self)
        print(f'создана категория {name}')

    @classmethod
    def print_instances(cls):
        for instance in cls.instances:
            print(instance.name)

    def create_category(self):
        return self
