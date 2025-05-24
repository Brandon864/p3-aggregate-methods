# lib/models.py
from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:
            return 0.0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses if num_courses > 0 else 0.0

class Enrollment:
    all = []

    def __init__(self, student, course, enrollment_date=None):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date or datetime.now()
        Enrollment.all.append(self)
        student._enrollments.append(self)

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

class Course:
    def __init__(self, name):
        self.name = name