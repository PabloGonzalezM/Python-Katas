import unittest
from random import random

from kata_03_opposite_number.opposite_number import opposite, lambda_opposite


class TestOppositeNumber(unittest.TestCase):

	def test_opposite_number(self):
		input_data = random()*100
		input_data_integer = int(input_data)

		self.assertEqual(opposite(input_data), -input_data)
		self.assertEqual(opposite(input_data_integer), -input_data_integer)

		self.assertEqual(lambda_opposite(input_data), -input_data)
		self.assertEqual(lambda_opposite(input_data_integer), -input_data_integer)

	def test_opposite_of_zero_is_zero(self):
		self.assertEqual(opposite(0), 0)

		self.assertEqual(lambda_opposite(0), 0)

	def test_wrong_type(self):
		data = "bad_input"
		with self.assertRaises(TypeError):
			opposite(data)

		with self.assertRaises(TypeError):
			lambda_opposite(data)


if __name__ == '__main__':
	unittest.main()
