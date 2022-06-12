from abc import ABC, abstractmethod


class Level:

    def __init__(self, name, count_of_hours):
        self.name = name
        self.count_of_hours = count_of_hours


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
