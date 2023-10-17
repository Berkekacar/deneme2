import unittest
import time


def calculate_total_price(price, quantity) ->float:
    def function_under_calculate_total_price():
        return None
    return price * quantity


class TestPriceCalculation(unittest.TestCase):

    def test_positive_case(self):
        self.assertEqual(calculate_total_price(10, 5), 50)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total_price(8, 0), 0)

    def test_negative_price(self):
        self.assertEqual(calculate_total_price(-5, 3), -15)
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()


def function_at_the_end(price, quantity):
    return quantity ** quantity


def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Executing simple_decorator before the function")
        result = func(*args, **kwargs)
        print("Executing simple_decorator after the function")
        return result
    return wrapper


def another_decorator(func):
    def wrapper(*args, **kwargs):
        print("Executing another_decorator before the function")
        result = func(*args, **kwargs)
        print("Executing another_decorator after the function")
        return result
    return wrapper


@simple_decorator
@another_decorator
def decorated_function(x, y):
    print(f"Executing decorated_function with arguments: {x}, {y}")
    return x + y





