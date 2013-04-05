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
		self.assertEqual(len(header), len(data[0]),
			"header and data column size doesn't match")
		self.assertEqual(len(data[0]), 6, 
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
		self.assertEqual(len(header), len(data[0]),
			"header and data column size doesn't match")
		self.assertEqual(len(data), 2, 
			"incorrect number of authors")
		self.assertEqual(data[0][-1], 1, 
			"incorrect total")

	def test_get_publications_by_year(self):
		db = database.Database()
		db.read("../data/simple.xml")
		header, data = db.get_publications_by_year()
		self.assertEqual(len(header), len(data[0]),
			"header and data column size doesn't match")
		self.assertEqual(len(data), 1,
			"incorrect number of rows")
		self.assertEqual(data[0][0], 9999,
			"incorrect year in result")

	def test_get_author_totals_by_year(self):
		db = database.Database()
		db.read("../data/simple.xml")
		header, data = db.get_author_totals_by_year()
		self.assertEqual(len(header), len(data[0]),
			"header and data column size doesn't match")
		self.assertEqual(len(data), 1,
			"incorrect number of rows")
		self.assertEqual(data[0][0], 9999,
			"incorrect year in result")
		self.assertEqual(data[0][1], 2,
			"incorrect number of authors in result")

if __name__ == '__main__':
	unittest.main()

