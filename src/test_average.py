import unittest

import average

class TestAverage(unittest.TestCase):

	def setUp(self):
		pass

	def test_mean_is_zero_for_empty_dataset(self):
		self.assertEqual(average.mean([]), 0)

	def test_mean_is_correct_for_single_value(self):
		self.assertEqual(average.mean([1]), 1)
	
	def test_mean_is_correct_for_known_output(self):
		self.assertEqual(average.mean([1,2,3]), 2)

	def test_mean_returns_real_number(self):
		self.assertEqual(average.mean([1,2]), 1.5)

	def test_median_is_zero_for_empty_dataset(self):
		self.assertEqual(average.median([]), 0)

	def test_median_is_correct_for_single_value(self):
		self.assertEqual(average.median([1]), 1)

	def test_median_is_correct_in_sorted_dataset(self):
		self.assertEqual(average.median([1,2,3]), 2)

	def test_median_is_correct_for_even_numbers_of_elements(self):
		self.assertEqual(average.median([1,2]), 1.5)

	def test_mode_is_zero_for_empty_dataset(self):
		self.assertEqual(average.mode([]), 0)

	def test_mode_is_correct_for_known_values(self):
		self.assertEqual(average.mode([1,2,2,3], 2)

	def test_mode_is_zero_for_bimodal_dataset(self):
		self.assertEqual(average.mode([1,1,2,2]), 0)

	def test_mode_is_zero_for_multimodal_dataset(self):
		self.assertEqual(average.mode([1,1,2,2,3,3]), 0)

if __name__ == '__main__':
	unittest.main()

