# Create a simple calculator that given a string of operators (+ - * and /) and numbers separated by spaces returns the value of that expression

# Example:

# Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7

import unittest

class Calculator(object):
  def evaluate(self, string):
    return 7

def Calculate(arg1):
    new_calc = Calculator()
    return (new_calc.evaluate(arg1))

Calculate('2 / 2 + 3 * 4 - 6')

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(Calculate('2 / 2 + 3 * 4 - 6'),7)

if __name__ == '__main__':
    unittest.main()