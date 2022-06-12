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

    def __init__(self, street: str, num_building: int, audithory: int):
        self.street = street
        self.num_building = num_building
        self.auditory = audithory
        print(f'Адрес улица: {street} дом: {num_building} аудитория: {audithory}')


class OnLine:

    def __init__(self, type_course, address, name, main_site):
        self.type_course = type_course
        self.address = address
        self.web_system = WebSystem(name, main_site)
        print(f'тип онлайн по адресу: {address}')


class OffLine:

    def __init__(self, type_course, street, num_building, audithory):
        self.type_course = type_course
        self.address = Address(street, num_building, audithory)
        print(f'Тип курса: {type_course}')


class AbstractType(ABC):

    @abstractmethod
    def create_type_online(self, type_course, address, name, main_site):
        pass

    @abstractmethod
    def create_type_offline(self, type_cource, street, num_building, audithory):
        pass


class TypeCourse(AbstractType):

    @staticmethod
    def create_type_online(type_course='online', address='some linc', name='websystem', main_site='www.webinar.ru'):
        return OnLine(type_course, address, name, main_site)

    @staticmethod
    def create_type_offline(type_course='offline', street='street', num_building=0, audithory=0):
        return OffLine(type_course, street, num_building, audithory)
