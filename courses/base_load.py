import sys

from courses.types_course import TypeCourse

load_categories = {
    'Python': 'python',
    'Java': 'java'
}

load_levels = {
    'junior': 'junior',
    'middle': 'middle',
    'senior': 'senior'
}

load_types = {
    'online': TypeCourse.create_type_online,
    'offline': TypeCourse.create_type_offline
}