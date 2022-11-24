import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    #suma
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
            self.assertRaises(TypeError, self.calc.add, "2", 2)
            self.assertRaises(TypeError, self.calc.add, 2, "2")
            self.assertRaises(TypeError, self.calc.add, "2", "2")
            self.assertRaises(TypeError, self.calc.add, None, 2)
            self.assertRaises(TypeError, self.calc.add, 2, None)
            self.assertRaises(TypeError, self.calc.add, object(), 2)
            self.assertRaises(TypeError, self.calc.add, 2, object())
    #resta
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(2, self.calc.substract(4, 2))
        self.assertEqual(-6, self.calc.substract(-4, 2))
        self.assertEqual(6, self.calc.substract(4, -2))
        self.assertEqual(1, self.calc.substract(1, 0))

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, None, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())
        self.assertRaises(TypeError, self.calc.substract, object(), object())

    #multiplicacion
    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, None, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        self.assertRaises(TypeError, self.calc.multiply, object(), object())


    #division
    def test_divide_method_returns_correct_result(self):
            self.assertEqual(1, self.calc.divide(2, 2))
            self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, None, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())
        self.assertRaises(TypeError, self.calc.divide, object(), object())

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    #raiz cuadrada
    def test_squareroot_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.squareroot(9))
        self.assertEqual(4, self.calc.squareroot(16))
        self.assertEqual(5, self.calc.squareroot(25))
        self.assertEqual(0, self.calc.squareroot(0))

    def test_squareroot_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.squareroot, "2")
        self.assertRaises(TypeError, self.calc.squareroot, None)
        self.assertRaises(TypeError, self.calc.squareroot, object())

    def test_squareroot_method_fails_with_x_minor_zero(self):
        self.assertRaises(TypeError, self.calc.squareroot, -1)
        self.assertRaises(TypeError, self.calc.squareroot, -2)
        self.assertRaises(TypeError, self.calc.squareroot, -3)


    #potenciacion
    def test_power_method_returns_correct_result(self):
        self.assertEqual(256, self.calc.power(4, 4))
        self.assertEqual(3125, self.calc.power(5, 5))
        self.assertEqual(1, self.calc.power(1, 1))
        self.assertEqual(1, self.calc.power(1, 2))
        self.assertEqual(1, self.calc.power(1, 0))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, None, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
        self.assertRaises(TypeError, self.calc.power, object(), object())

    #log10
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))

    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())

    def test_log10_method_fails_with_x_minor_or_equals_zero(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -0)
        self.assertRaises(TypeError, self.calc.log10, -1)
        self.assertRaises(TypeError, self.calc.log10, -2)


   

    

    

    

    


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
