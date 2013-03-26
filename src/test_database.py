import database
import unittest

class TestDatabase(unittest.TestCase):

	def setUp(self):
		pass

	def test_read(self):
		db = database.Database()
		db.read("../data/simple.xml")
		self.assertEqual(len(db.publications), 1)

	def test_get_publication_summary(self):
		db = database.Database()
		db.read("../data/simple.xml")
		header, data = db.get_publication_summary()
		self.assertEqual(len(data[0]), 5, 
			"incorrect number of columns in data")
		self.assertEqual(len(data), 2, 
			"incorrect number of rows in data")
		self.assertEqual(data[0][1], 1, 
			"incorrect number of publications for conference papers")
		self.assertEqual(data[1][1], 2, 
			"incorrect number of authors for conference papers")

	def test_get_publications_by_author(self):
		db = database.Database()
		db.read("../data/simple.xml")
		header, data = db.get_publications_by_author()
		self.assertEqual(len(data), 2, 
			"incorrect number of authors")

	def test_get_publications_by_year(self):
		db = database.Database()
		db.read("../data/simple.xml")
		self.assertTrue(False)

	def test_get_author_totals_by_year(self):
		db = database.Database()
		db.read("../data/simple.xml")
		self.assertTrue(False)

if __name__ == '__main__':
	unittest.main()

