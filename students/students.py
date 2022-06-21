from abc import ABC, abstractmethod
from courses.notify import Subscriber
from courses.courses import CoursesFactory

class AbstractStudent(ABC):
    instances = []

    def __init__(self, name, surname, email, tel_num):
        self.__class__.instances.append(self)
        self.name = name
        self.surname = surname
        self.email = email
        self.tel_num = tel_num
        self.courses = []

    @abstractmethod
    def add_course(self, course):
        pass

    def __str__(self):
        all_courses = ''
        for course in self.courses:
            # print(course.category_course.name)
            all_courses = all_courses + " " + course.category_course.name + " " + course.level_course.name \
                          + " " + course.type_course.type_course + ','
        return f' Name: {self.name}, Surname: {self.surname}, E-mail: {self.email}, Tel: {self.tel_num},' \
               f' \n Courses: {all_courses}'


class Students(AbstractStudent, Subscriber):
    def add_course(self, course):
        self.courses.append(course)
        self.notify(course)
        print(f'печатаем объект: {self}')
        student = self
        CoursesFactory.subscribe(self)
        # print(f' add in list: {self.courses}')
        return self

    def notify(self, course):
        print(f'Студент {self.name} записан на курс {course.category_course.name}')
