import sqlite3

from orm.domain_object import Person
from orm.person_mapper import PersonMapper

connection = sqlite3.connect('patterns.sqlite')


class MapperRegistry:
    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, Person):
            return PersonMapper(connection)


class CategoryMapper:
    pass