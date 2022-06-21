from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def notify(self, course):
        pass


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, courier):
        pass

    @abstractmethod
    def unsubscribe(self, courier):
        pass


