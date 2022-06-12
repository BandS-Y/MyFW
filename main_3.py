from courses.courses import CoursesFactory
import random


load_categories = ['Python', 'Java', 'JavaScript']
load_levels = ['junior', 'middle', 'senior']
load_types = ['online', 'offline']

courses = []

for i in range(10):
    course = CoursesFactory(load_categories[random.randint(0, 2)],
                            load_types[random.randint(0, 1)],
                            load_levels[random.randint(0, 1)])
    courses.append(course)

for category_isinstance in CoursesFactory.instances:
    print(category_isinstance.category_course.name, category_isinstance.level_course.name,
          category_isinstance.type_course.type_course)
