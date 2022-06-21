import sys
from abc import ABC, abstractmethod

from courses import base_load
from courses.category import CategoryCourse
from courses.notify import Publisher

sys.path.append('../')

import courses.base_load
import courses.types_course


class AbstractCourses(ABC):

    def create_type(self, type_course):
        pass


class CoursesFactory(AbstractCourses, Publisher):
    instances = []

    def __init__(self, name, type_course=None, level_course=None):
        self.__class__.instances.append(self)
        self.category_course = self.create_category(name)
        if type_course in base_load.load_types:
            self.type_course = self.create_type(type_course)
        if level_course in base_load.load_levels:
            self.level_course = self.create_level(level_course)
        self.student = set()

    @classmethod
    def print_instances(cls):
        for instance in cls.instances:
            print(instance)

    def create_type(self, type_course):
        if type_course in base_load.load_types:
            return base_load.load_types[type_course]()
        else:
            return None

    @staticmethod
    def create_category(name):
        if name in base_load.load_categories:
            return CategoryCourse(name)
        else:
            return None

    @staticmethod
    def create_level(level):
        if level in base_load.load_levels:
            return base_load.load_levels[level]()
        else:
            return None

    def subscribe(self):
        self.student.add(student)

    def unsubscribe(self, student):
        self.student.discard(student)

