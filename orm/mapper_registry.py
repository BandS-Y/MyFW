from orm.connect import connection
import orm.domain_objects
from orm.mapper import PersonMapper, CategoryMapper, LevelMapper, TypeMapper


class MapperRegistry:
    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, orm.domain_objects.Person):
            return PersonMapper(connection)
        if isinstance(obj, orm.domain_objects.Category):
            return CategoryMapper(connection)
        if isinstance(obj, orm.domain_objects.Level):
            return LevelMapper(connection)
        if isinstance(obj, orm.domain_objects.Type):
            return TypeMapper(connection)


