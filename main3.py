from courses.category import CategoryCourse
from courses.courses import CoursesFactory

import courses.base_load


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
