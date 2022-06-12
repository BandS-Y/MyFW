from abc import ABC, abstractmethod


class Level(ABC):

    def __init__(self, name, count_of_hours):
        self.name = name
        self.count_of_hours = count_of_hours
        print(f'Создан уровень {name}')


class JuniorLevel(Level):

    def __init__(self, name, count_of_hours):
        super().__init__(name, count_of_hours)


class MiddleLevel(Level):

    def __init__(self, name, count_of_hours):
        super().__init__(name, count_of_hours)


class SeniorLevel(Level):

    def __init__(self, name, count_of_hours):
        super().__init__(name, count_of_hours)


class AbstractLevel(ABC):

    @abstractmethod
    def level_junior(self):
        pass

    @abstractmethod
    def level_middle(self):
        pass

    @abstractmethod
    def level_senior(self):
        pass


class LevelCourses(AbstractLevel):

    @staticmethod
    def level_junior():
        return JuniorLevel('Junior', 50)

    @staticmethod
    def level_middle():
        return MiddleLevel('Middle', 100)

    @staticmethod
    def level_senior():
        return SeniorLevel('Senior', 150)
