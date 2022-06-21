from courses.courses import CoursesFactory
import random

from students.students import Students

load_categories = ['Python', 'Java', 'JavaScript']
load_levels = ['junior', 'middle', 'senior']
load_types = ['online', 'offline']

courses = []

student0 = Students('Ivan', 'Ivanov', 'abc@mail.ru', '+7 913 231 23 45')
student1 = Students('Petr', 'Petrov', 'bcd@mail.ru', '+7 913 123 12 34')
student2 = Students('Nikolay', 'Sidor', 'cde@gmail.ru', '+7 913 345 67 78')
student3 = Students('Olga', 'Odina', 'efg@gmail.ru', '+7 913 123 45 67')

for i in range(10):
    course = CoursesFactory(load_categories[random.randint(0, 2)],
                            load_types[random.randint(0, 1)],
                            load_levels[random.randint(0, 1)])
    courses.append(course)

for category_isinstance in CoursesFactory.instances:
    print(category_isinstance.category_course.name, category_isinstance.level_course.name,
          category_isinstance.type_course.type_course)

courses_count = len(CoursesFactory.instances)
for student in Students.instances:
    for i in range(3):
        student.add_course(CoursesFactory.instances[random.randint(0, courses_count-1)])

for student in Students.instances:
    print(student)

