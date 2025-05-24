# lib/student.py
class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  # List of Enrollment instances
        self._grades = {}  # Dictionary mapping Enrollment to grade

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        if not self._grades:  # Handle case with no grades
            return 0.0
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses if num_courses > 0 else 0.0