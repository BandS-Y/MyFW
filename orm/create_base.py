import sqlite3

from domain_object import Person
from person_mapper import PersonMapper
from unit_of_work import UnitOfWork

connection = sqlite3.connect('patterns.sqlite')

if __name__ == '__main__':
    try:
        UnitOfWork.new_current()
        new_person_1 = Person(None, 'Igor', 'Igorev')
        new_person_1.mark_new()

        new_person_2 = Person(None, 'Fedor', 'Fedorov')
        new_person_2.mark_new()

        person_mapper = PersonMapper(connection)
        exists_person_1 = person_mapper.find_by_id(1)
        exists_person_1.mark_dirty()
        print(exists_person_1.first_name)
        exists_person_1.first_name += ' Senior'
        print(exists_person_1.first_name)

        exists_person_2 = person_mapper.find_by_id(2)
        exists_person_2.mark_removed()

        print(UnitOfWork.get_current().__dict__)

        UnitOfWork.get_current().commit()
    except Exception as e:
        print(e.args)
    finally:
        UnitOfWork.set_current(None)

    print(UnitOfWork.get_current())
