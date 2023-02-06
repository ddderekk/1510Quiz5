from unittest import TestCase
from calculate_pay import calculate_pay


class TestCalculatePay(TestCase):
    def test_calculate_pay_40_hours_and_float(self):
        self.assertEqual(620.0, calculate_pay(40, 15.5))

    def test_calculate_hours_zero(self):
        self.assertEqual(0.0, calculate_pay(0, 10))

    def test_calculate_wage_zero(self):
        self.assertEqual(0.0, calculate_pay(10, 0))

    def test_calculate_floats_negative_hours(self):
        self.assertEqual(0.0, calculate_pay(-10, 15.50))
