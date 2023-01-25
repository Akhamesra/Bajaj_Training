import unittest
from calc import Calculator

class TestCalc(unittest.TestCase):
    def test_sum(self):
        c = Calculator(9,6)
        self.assertEqual(c.get_addition(), 15, 'The sum is wrong')

if __name__ == '__main__':
    unittest.main()