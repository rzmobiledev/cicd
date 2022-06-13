"""
Sample test
"""
from django.test import SimpleTestCase
from admin import calc


class CalcTest(SimpleTestCase):
    """Test calc module"""
    def test_add_number(self):
        res = calc.add(10, 4)
        self.assertEqual(res, 14)

    def test_substract_number(self):
        res = calc.substract(5, 3)
        self.assertEqual(res, 2)