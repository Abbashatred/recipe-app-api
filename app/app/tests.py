from django.test import SimpleTestCase
from . import calc

class JustTest(SimpleTestCase):

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)