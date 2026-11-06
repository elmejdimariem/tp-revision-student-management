import unittest
from student_manager import (
    calculate_average,
    get_mention,
    is_admitted,
    validate_grades,
)


class TestStudentManager(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([12, 15, 18]), 15)

    def test_calculate_average_identical(self):
        self.assertEqual(calculate_average([10, 10, 10]), 10)

    def test_calculate_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_mention_echec(self):
        self.assertEqual(get_mention(8), "Échec")

    def test_mention_bien(self):
        self.assertEqual(get_mention(15), "Bien")

    def test_mention_excellent(self):
        self.assertEqual(get_mention(18), "Excellent")

    def test_admitted(self):
        self.assertTrue(is_admitted(12))

    def test_not_admitted(self):
        self.assertFalse(is_admitted(9))

    def test_valid_grades(self):
        self.assertTrue(validate_grades([12, 15, 18]))

    def test_invalid_empty(self):
        self.assertFalse(validate_grades([]))

    def test_invalid_above_20(self):
        self.assertFalse(validate_grades([12, 25, 18]))

    def test_invalid_negative(self):
        self.assertFalse(validate_grades([-2, 12, 15]))

    def test_average_ten_is_admitted(self):
        self.assertTrue(is_admitted(10))


if __name__ == "__main__":
    unittest.main()