import unittest

from marks import calculate_grade, calculate_percentage


class MarksTest(unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(calculate_percentage([80, 90, 100]), 90)

    def test_invalid_marks(self):
        for marks in ([], [-1], [101]):
            with self.assertRaises(ValueError):
                calculate_percentage(marks)

    def test_grade(self):
        self.assertEqual(calculate_grade(80), 10)
        self.assertEqual(calculate_grade(60), 8)
        self.assertEqual(calculate_grade(40), 6)
        self.assertEqual(calculate_grade(39.9), 0)


if __name__ == "__main__":
    unittest.main()
