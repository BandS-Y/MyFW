import sys
from abc import ABC, abstractmethod
sys.path.append('../')
import courses.base_load


class WebSystem:

    def __init__(self, name: str, main_site: str):
        self.name = name
        self.main_site = main_site
        print(f'Вебинарная система: {name} с основным сайтом {main_site}')


class Address:

    def __init__(self, street, num_building, auditory):
        self.street = street
        self.num_building = num_building
        self.auditory = auditory
        print(f'Адрес улица: {street} дом: {num_building} аудитория: {auditory}')


class OnLine:

    def __init__(self, address, name, main_site):
        self.address = address
        self.web_system = WebSystem(name, main_site)
        print(f'тип онлайн по адресу: {address}')


class OffLine:

    def __init__(self, name, street, num_building, auditory):
        self.name = name
        self.address = Address(street, num_building, auditory)
        print(f'{name}')


class AbstractType(ABC):

    @abstractmethod
    def create_type_online(self, address, name, main_site):
        pass

    @abstractmethod
    def create_type_offline(self, name, num_building, auditory):
        pass


class TypeCourse(AbstractType):

    @staticmethod
    def create_type_online(address='some linc', name='websystem', main_site='www.webinar.ru'):
        return OnLine(address, name, main_site)

    @staticmethod
    def create_type_offline(street='street', num_building=0, auditory=0):
        return OffLine(street, num_building, auditory)
