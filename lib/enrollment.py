# lib/enrollment.py
from datetime import datetime

class Enrollment:
    all = []

    def __init__(self, student, course, enrollment_date=None):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date or datetime.now()
        Enrollment.all.append(self)
        student._enrollments.append(self)  # Link to student

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count