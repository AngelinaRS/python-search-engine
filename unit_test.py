import application
import unittest

class SearchEngineTest(unittest.TestCase):

	def test_is_space(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.is_space(""), True)
		self.assertEqual(searcher.is_space(" "), True)
		self.assertEqual(searcher.is_space("dulce"), False)

	def test_valid_url(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.valid_url("fdfdfsedeee4fds"), False)

	def test_count_page(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.count_page("a", "aba"), 2)

	def test_minuscule(self):
		searcher = application.SearchEngine()
		self.assertEqual(searcher.minuscule("Y"), "y")

if __name__ == '__main__':
	unittest.main()