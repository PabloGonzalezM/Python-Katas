import unittest

from kata_04_remove_first_and_last_character.remove_first_and_last_character import remove_char, lambda_remove_char


class TestOppositeNumber(unittest.TestCase):

	def test_opposite_number(self):
		input_data = "Hello everyone"
		output_data = "ello everyon"

		self.assertEqual(remove_char(input_data), output_data)

		self.assertEqual(lambda_remove_char(input_data), output_data)

	def test_wrong_type(self):
		input_data = 5
		with self.assertRaises(TypeError):
			remove_char(input_data)

		with self.assertRaises(TypeError):
			lambda_remove_char(input_data)


if __name__ == '__main__':
	unittest.main()
