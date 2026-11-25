import unittest
from registration import register_student

class TestRegistration(unittest.TestCase):

    def test_successful_registration(self):
        result = register_student("Naif", "Software Engineering")
        self.assertEqual(result, "Registration successful")

    def test_empty_student_name(self):
        result = register_student("", "Software Engineering")
        self.assertEqual(result, "Registration failed")

    def test_empty_course(self):
        result = register_student("Naif", "")
        self.assertEqual(result, "Registration failed")


if __name__ == "__main__":
    unittest.main()
