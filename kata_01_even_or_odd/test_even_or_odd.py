import unittest
from random import randrange

from kata_01_even_or_odd.even_or_odd import even_or_odd, lambda_even_or_odd


class TestEvenOrOdd(unittest.TestCase):

	def test_is_even(self):
		self.assertEqual(even_or_odd(randrange(-100, 100, 2)), 'Even')
		self.assertEqual(lambda_even_or_odd(randrange(-100, 100, 2)), 'Even')

	def test_is_odd(self):
		self.assertEqual(even_or_odd(randrange(-99, 99, 2)), 'Odd')
		self.assertEqual(lambda_even_or_odd(randrange(-99, 99, 2)), 'Odd')

	def test_wrong_type(self):
		data = "bad_input"
		with self.assertRaises(TypeError):
			even_or_odd(data)

		with self.assertRaises(TypeError):
			lambda_even_or_odd(data)


if __name__ == '__main__':
	unittest.main()
