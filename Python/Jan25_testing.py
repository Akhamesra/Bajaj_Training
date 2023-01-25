# UNIT TESTING in python

#ASSERT TESTING
'''
assert 1>0 -> TRUE
assert 1<0 -> Assertion Error
'''
'''
x = int(input("Enter a number : "))
try:
    assert x>0, "Wrong number"
    print("Yes")
except AssertionError as ae:
    print(ae)
'''

#ASSERT METHODS
'''
assertEqual(x, y, msg=None)	        x == y
assertNotEqual(x,y,msg=None)	    x != y
assertTrue(x, msg=None)	            bool(x) is True
assertFalse(x, msg=None)	        bool(x) is False
assertIs(x, y , msg=None)	        x is y
assertIsNot(x, y, msg=None)	        x is not y
assertIsNone(x, msg=None)	        x is None
assertIsNotNone(x , msg=None)	    x is not None
assertIn(x, y, msg=None)	        x in y
assertNotIn(x, y, msg=None)	        x not in y
assertIsInstance(x, y, msg=None)	isinstance(x, y)
assertNotIsInstance(x, y, msg=None)	not isinstance(x, y)
'''
# TESTING CALC>PY
import unittest
from calc import Calculator
'''
class TestCalc(unittest.TestCase):
    def test_sum(self):
        c = Calculator(9,6)
        self.assertEqual(c.get_addition(), 15, 'The sum is wrong')

if __name__ == '__main__':
    unittest.main()
'''

'''
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.c =Calculator(9,6)
        self.f = open("file.txt","r")
    def turnDown(self):
        self.f.close()
    def test_diff(self):
        self.assertEqual(self.c.get_difference(),3,'The diff is wrong')

if __name__ == '__main__':
    unittest.main()
'''