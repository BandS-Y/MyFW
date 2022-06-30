from orm.connect import connection
import orm.domain_objects
from orm.mapper import PersonMapper
from orm.unit_of_work import UnitOfWork

try:
    # print(globals())
    UnitOfWork.new_current()
    new_person_1 = orm.domain_objects.Person(None, 'Igor', 'Igorev')
    new_person_1.mark_new()

    new_person_2 = orm.domain_objects.Person(None, 'Fedor', 'Fedorov')
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


try:
    UnitOfWork.new_current()
    new_person_1 = orm.domain_objects.Person(None, 'Igor', 'Igorev')
    new_person_1.mark_new()

    print(UnitOfWork.get_current().__dict__)

    UnitOfWork.get_current().commit()

except Exception as e:
    print(e.args)
finally:
    UnitOfWork.set_current(None)

print(UnitOfWork.get_current())


# try:
#     print(UnitOfWork.get_current())
#     UnitOfWork.new_current()
#     new_category = Category(None, 'Basic')
#     new_category.mark_new()
#
#     print(UnitOfWork.get_current().__dict__)
#
#     UnitOfWork.get_current().commit()
#
# except Exception as e:
#     print(e.args)
# finally:
#     UnitOfWork.set_current(None)
#
# print(UnitOfWork.get_current())


# try:
#     print(UnitOfWork.get_current())
#     UnitOfWork.new_current()
#     new_category = Level(None, 'MAX')
#     new_category.mark_new()
#
#     # category_mapper = CategoryMapper(connection)
#     # exists_category = category_mapper.find_by_id(2)
#     # exists_category.mark_dirty()
#     # print(exists_category.name)
#
#     print(UnitOfWork.get_current().__dict__)
#     UnitOfWork.get_current().commit()
#
# except Exception as e:
#     print(e.args)
# finally:
#     UnitOfWork.set_current(None)
#
# print(UnitOfWork.get_current())

# try:
#     print(UnitOfWork.get_current())
#     UnitOfWork.new_current()
#     new_category = Type(None, 'Combo')
#     new_category.mark_new()
#
#     # category_mapper = CategoryMapper(connection)
#     # exists_category = category_mapper.find_by_id(2)
#     # exists_category.mark_dirty()
#     # print(exists_category.name)
#
#     print(UnitOfWork.get_current().__dict__)
#     UnitOfWork.get_current().commit()
#
# except Exception as e:
#     print(e.args)
# finally:
#     UnitOfWork.set_current(None)
#
# print(UnitOfWork.get_current())

try:
    UnitOfWork.new_current()
    new_person_1 = orm.domain_objects.Person(None, 'Igor', 'Igorev')
    new_person_1.mark_new()

    print(UnitOfWork.get_current().__dict__)

    UnitOfWork.get_current().commit()

except Exception as e:
    print(e.args)
finally:
    UnitOfWork.set_current(None)

print(UnitOfWork.get_current())