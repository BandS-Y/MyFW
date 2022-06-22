
from orm.unit_of_work import UnitOfWork


class DomainObject:

    def mark_new(self):
        UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        UnitOfWork.get_current().register_removed(self)


class Person(DomainObject):
    def __init__(self, id_person, first_name, last_name):
        self.id_person = id_person
        self.last_name = last_name
        self.first_name = first_name


class Category(DomainObject):
    def __init__(self, name):
        self.name = name

