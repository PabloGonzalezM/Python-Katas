import unittest

from kata_02_sum_of_positive.sum_of_positive import positive_sum, lambda_positive_sum


class TestSumOfPositives(unittest.TestCase):

	def test_sum_of_all_positives_is_valid(self):
		input_data_integers = [1, -2, 3, 4, 5]
		input_data_floats = [1.1, -2.1, 3.1, 4.1, 5.1]
		input_data_mix = [1.1, -2, 3, 4.1, 5]

		self.assertEqual(positive_sum(input_data_integers), 13)
		self.assertEqual(positive_sum(input_data_floats), 13.4)
		self.assertEqual(positive_sum(input_data_mix), 13.2)

		self.assertEqual(lambda_positive_sum(input_data_integers), 13)

	def test_sum_of_all_negatives_is_zero(self):
		input_data_negatives = [-1, -2, -3, -4, -5]

		self.assertEqual(positive_sum(input_data_negatives), 0)

		self.assertEqual(lambda_positive_sum(input_data_negatives), 0)

	def test_sum_of_empty_array_is_zero(self):
		self.assertEqual(positive_sum([]), 0)

		self.assertEqual(lambda_positive_sum([]), 0)

	def test_wrong_type(self):
		data = "bad_input"
		with self.assertRaises(TypeError):
			positive_sum(data)

		with self.assertRaises(TypeError):
			lambda_positive_sum(data)


if __name__ == '__main__':
	unittest.main()
