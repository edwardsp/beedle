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
		self.year = int(year)
		self.authors = authors

class Author:
	def __init__(self, name):
		self.name = name

class Database:
	def read(self, filename):
		self.publications = []
		self.authors = []
		self.author_idx = {}
		self.publications_by_author = {}

		handler = DocumentHandler(self)
		parser = make_parser()
		parser.setContentHandler(handler)
		infile = open(filename)
		parser.parse(infile)
		infile.close()


	def get_publication_summary(self):
		header = ( "Details", "Conference Paper", 
			"Journal", "Book", "Book Chapter" )

		plist = [0,0,0,0]
		alist = [set(),set(),set(),set()]

		for p in self.publications:
			plist[p.pub_type] += 1
			for a in p.authors:
				alist[p.pub_type].add(a)
		data = [
			["Number of publications"] + plist,
			["Number of authors"] + [ len(a) for a in alist ] ]
		return (header, data)

	def get_publications_by_author(self):
		header = ( "Author", "Number of conference papers",
			"Number of journals", "Number of books",
			"Number of book chapers", "Total" )

		astats = [ [0,0,0,0] for i in range(len(self.authors)) ]
		for p in self.publications:
			for a in p.authors:
				astats[a][p.pub_type] += 1

		data = [ [self.authors[i].name] + astats[i] + [sum(astats[i])] 
			for i in range(len(astats)) ]
		return (header, data)

	def get_publications_by_year(self):
		header = ( "Year", "Number of conference papers",
			"Number of journals", "Number of books",
			"Number of book chapers" )

		ystats = {}
		for p in self.publications:
			try:
				ystats[p.year][p.pub_type] += 1
			except KeyError:
				ystats[p.year] = [0,0,0,0]
				ystats[p.year][p.pub_type] += 1

		data = [ [y]+ystats[y] for y in ystats ]
		return (header, data)	

	def get_author_totals_by_year(self):
		header = ( "Year", "Number of conference papers",
			"Number of journals", "Number of books",
			"Number of book chapers" )

		ystats = {}
		for p in self.publications:
			try:
				s = ystats[p.year][p.pub_type]
			except KeyError:
				ystats[p.year] = [set(), set(), set(), set()]
				s = ystats[p.year][p.pub_type]
			for a in p.authors:
				s.add(a)
		data = [ [y]+[len(s) for s in ystats[y]]
			for y in ystats ]
		return (header, data)	

	def add_publication(self, pub_type, title, year, authors):
		idlist = []
		for a in authors:
			try:
				idlist.append(self.author_idx[a])
			except KeyError:
				idlist.append(len(self.authors))
				self.authors.append(Author(a))
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
			self.db.add_publication(
				self.pub_type,
				self.title,
				self.year,
				self.authors)
			self.clearData()

	def characters(self, chrs):
		d = chrs.strip()
		if d == "":
			pass
		elif self.tag == "author":
			self.authors.append(d)
		elif self.tag == "title":
			self.title = d
		elif self.tag == "year":
			self.year = d


