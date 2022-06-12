import sys

from courses.types_course import TypeCourse
from courses.levels import LevelCourses

load_categories = {
    'Python': 'python',
    'Java': 'java',
    'JavaScript': 'javascript'
}

load_levels = {
    'junior': LevelCourses.level_junior,
    'middle': LevelCourses.level_middle,
    'senior': LevelCourses.level_senior
}

load_types = {
    'online': TypeCourse.create_type_online,
    'offline': TypeCourse.create_type_offline
}