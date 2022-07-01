import orm.domain_objects
from orm.connect import connection
from orm.mapper import PersonMapper, CategoryMapper, LevelMapper, TypeMapper
from orm.unit_of_work import UnitOfWork

try:
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
    new_category1 = orm.domain_objects.Category(None, 'Basic1')
    new_category1.mark_new()

    new_category2 = orm.domain_objects.Category(None, 'Basic2')
    new_category2.mark_new()

    print(UnitOfWork.get_current().__dict__)

    UnitOfWork.get_current().commit()

except Exception as e:
    print(e.args)
finally:
    UnitOfWork.set_current(None)

print(UnitOfWork.get_current())


try:
    UnitOfWork.new_current()
    new_category = orm.domain_objects.Level(None, 'MAX')
    new_category.mark_new()

    level_mapper = LevelMapper(connection)
    exists_level = level_mapper.find_by_id(2)
    exists_level.mark_dirty()
    print(exists_level.name)

    print(UnitOfWork.get_current().__dict__)
    UnitOfWork.get_current().commit()

except Exception as e:
    print(e.args)
finally:
    UnitOfWork.set_current(None)

print(UnitOfWork.get_current())

try:
    UnitOfWork.new_current()
    new_type = orm.domain_objects.Type(None, 'Combo')
    new_type.mark_new()

    type_mapper = TypeMapper(connection)
    exists_type = type_mapper.find_by_id(2)
    exists_type.mark_dirty()
    print(exists_type.name)

    print(UnitOfWork.get_current().__dict__)
    UnitOfWork.get_current().commit()

except Exception as e:
    print(e.args)
finally:
    UnitOfWork.set_current(None)

print(UnitOfWork.get_current())
