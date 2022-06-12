import sys
from abc import ABC, abstractmethod

from courses import base_load
from courses.category import CategoryCourse

sys.path.append('../')

import courses.base_load
import courses.types_course


class AbstractCourses(ABC):

    def create_type(self, type_course):
        pass


class CoursesFactory:

    @staticmethod
    def create_type(type_course):
        if type_course in base_load.load_types:
            return base_load.load_types[type_course]()

    @staticmethod
    def create_category(name):
        if name in base_load.load_categories:
            return CategoryCourse(name)
