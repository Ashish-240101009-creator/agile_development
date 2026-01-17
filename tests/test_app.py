import unittest
from src.app import MarksSystem

class TestSprint1(unittest.TestCase):

    def test_add_student_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        self.assertIn("101", ms.students)

    def test_add_student_duplicate(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_student("101", "Asha Again")

    def test_add_marks_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        ms.add_marks("101", 88)
        self.assertEqual(ms.students["101"].marks, 88)

    def test_add_marks_out_of_range(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_marks("101", 120)
    def test_calculate_grade_A_plus(self):
        ms = MarksSystem()
        ms.add_student("201", "Ravi")
        ms.add_marks("201", 95)
        self.assertEqual(ms.calculate_grade("201"), "A+")
    def test_generate_report_header(self):
        ms = MarksSystem()
        ms.add_student("301", "Kiran")
        report = ms.generate_report()
        self.assertIn("ROLL", report)
