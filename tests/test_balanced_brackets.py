import unittest
from parameterized import parameterized
from balanced_brackets import are_brackets_balanced

class BracketsBalancedTest(unittest.TestCase):

  @parameterized.expand([
    ('simple equation','1*(2+3)', True),
    ('simple equation','{1+3} * {7-2}', True),
    ('simple equation unclosed','(1+3) * (7-2', False),
    ('simple equation multiple unclosed','(1+3 * (7-2', False),
    ('multiple brackets unnested','(8/2) + [9*4] - {15/3}', True),
    ('multiple brackets nested','(1 + {3*7}) * [(4+6)*{12-5}]', True),
    ('multiple brackets multilevel nesting','(1 * {25 / [2 + 3]})', True),
    ('multiple brackets incorrect order','({1+2) * 5}', False),
    ('multiple brackets nested unopened','(1 + 3*7}) * [(4+6)*{12-5}]', False),
    ('multiple brackets nested multiple unopened','(1 + 3*7}) * [4+6)*{12-5}]', False)
  ])
  def test_matching_brackets(self, name, input_value, expected):
    self.longMessage = True
    actual = are_brackets_balanced(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)

  @parameterized.expand([
    ('no brackets','5 * 4', True),
    ('no brackets','1 + 2', True),
    ('no brackets','7 - 3 + 4', True),
    ('no brackets','21 + 10 / 5 - 6', True)
  ])
  def test_edge_cases(self, name, input_value, expected):
    self.longMessage = True
    actual = are_brackets_balanced(input_value)
    message = 'For input {0}, expected value = {1}, and actual value = {2}'.format(input_value, expected, actual)
    self.assertEqual(expected, actual, message)