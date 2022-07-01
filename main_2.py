from courses.category import CategoryCourse
from courses.courses import CoursesFactory

import courses.base_load

#
# for i in range(5):
#     course = courses
courses0 = {
    'course0': {
        'course': 'CoursesFactory',
        'course_type': 'create_type',
        'course_category': 'create_category'
            },
    'course1': {
        'course': 'CoursesFactory',
        'course_type': 'create_type',
        'course_category': 'create_category'
            }
}

courses1 = []

# for i in range(3):


# print(courses['course0'])
courses0['course0']['course'] = CoursesFactory
courses0['course0']['course_type'] = courses0['course0']['course'].create_type('online')
courses0['course0']['course_category'] = courses0['course0']['course'].create_category('Python')
print(courses)
# print(course)
# print(course.web_system.main_site)

course1 = CoursesFactory.create_category('Java')
course2 = CoursesFactory.create_category('Python')
print(CategoryCourse.print_instances())
print(CategoryCourse.instances)
for category_isinstance in CategoryCourse.instances:
    print(category_isinstance.name)

print(courses)
