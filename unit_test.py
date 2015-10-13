import application
import unittest

class SearchEngineTest(unittest.TestCase):

	def test_is_space(self):
		self.assertEqual(application.is_space(""), True)
		self.assertEqual(application.is_space(" "), True)
		self.assertEqual(application.is_space("dulce"), False)

	def test_valid_url(self):
		self.assertEqual(application.valid_url("fdfdfsedeee4fds"), False)

	def test_count_page(self):
		self.assertEqual(application.count_page("a", "aba"), 2)

if __name__ == '__main__':
	unittest.main()