import orm.unit_of_work


class DomainObject:

    def mark_new(self):
        orm.unit_of_work.UnitOfWork.get_current().register_new(self)

    def mark_dirty(self):
        orm.unit_of_work.UnitOfWork.get_current().register_dirty(self)

    def mark_removed(self):
        orm.unit_of_work.UnitOfWork.get_current().register_removed(self)


class Person(DomainObject):
    def __init__(self, id_person, first_name, last_name, email=None, telephone=None):
        self.id_person = id_person
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.telephone = telephone


class Category(DomainObject):
    def __init__(self, id_category, name):
        self.id_category = id_category
        self.name = name


class Level(DomainObject):
    def __init__(self, id_level, name):
        self.id_level = id_level
        self.name = name


class Type(DomainObject):
    def __init__(self, id_type, name):
        self.id_type = id_type
        self.name = name

