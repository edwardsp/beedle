from xml.sax import handler, make_parser

PublicationType = [
	"Conference Paper", "Journal", "Book", "Book Chapter"]

class Publication:
	CONFERENCE_PAPER = 0
	JOURNAL = 1
	BOOK = 2
	BOOK_CHAPTER = 3

	def __init__(self, pub_type, title, year, authors):
		self.pub_type = pub_type
		self.title = title
		self.year = year
		self.authors = authors

class Author:
	def __init__(self, name):
		self.name = name

class Database:
	def read(self, filename):
		publications = []
		authors = []
		author_idx = {}

	def get_publication_summary(self):
		pass

	def get_publications_by_author(self):
		pass

	def get_publications_by_year(self):
		pass

	def get_author_totals_by_year(self):
		pass

	def add_publication(self, pub_type, title, year, authors):
		idlist = []
		for a in authors:
			try:
				idlist.append(self.author_idx[a])
			catch KeyError:
				idlist.append(len(authors))
				authors.append(Author(a))
		self.publications.append(
			Publication(pub_type, title, year, idlist))

class DocumentHandler(handler.ContentHandler):
	PUB_TYPE = {
		"inproceedings":Publication.CONFERENCE_PAPER,
		"article":Publication.JOURNAL,
		"book":Publication.BOOK,
		"incollection":Publication.BOOK_CHAPTER }

	def __init__(self, db):
		self.tag = None
		self.clearData()
		self.db = db

	def clearData(self):
		self.pub_type = None
		self.authors = []
		self.year = None
		self.title = None

	def startDocument(self):
		pass

	def endDocument(self):
		pass

	def startElement(self, name, attrs):
		if name in DocumentHandler.PUB_TYPE.keys():
			self.pub_type = DocumentHandler.PUB_TYPE[name]
		self.tag = name
			
	def endElement(self, name):
		if name in DocumentHandler.PUB_TYPE.keys():
			self.dblp.add_publication(
				self.pub_type,
				self.title,
				self.year,
				self.authors)
			self.clearData()

	def characters(self, chrs):
		if tag == "author":
			self.authors.append(chrs.strip())
		elif tag == "title":
			self.title = chrs.strip()
		elif tag == "year":
			self.year = chrs.strip()


