from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def notify(self, order, service):
        pass


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, courier):
        pass

    @abstractmethod
    def unsubscribe(self, courier):
        pass


class Courier(Subscriber):
    def __init__(self, name):
        self.name = name

    def notify(self, order, service):
        print(f'Курьер {self.name} взял заказ {order}')
        service.unsubscribe(self)
        print('курьер поехал')


class Restaurant(Publisher):
    def __init__(self):
        self.couriers = set()

    def subscribe(self, courier):
        self.couriers.add(courier)

    def unsubscribe(self, courier):
        self.couriers.discard(courier)

    def dispatch(self, message):
        if len(self.couriers) == 0:
            print('нет свободных курьеров')
        else:
            for courier in self.couriers:
                courier.notify(message, self)
                break


pizza = Restaurant()
ivan = Courier('Ivan')
tom = Courier('Tom')

pizza.subscribe(ivan)
pizza.subscribe(tom)

pizza.dispatch('Пицца')
pizza.dispatch('Бургер')
pizza.dispatch('Кола')