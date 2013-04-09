from xml.sax import handler, make_parser, SAXException

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
		if year:
			self.year = int(year)
		else:
			self.year = -1
		self.authors = authors

class Author:
	def __init__(self, name):
		self.name = name

class Database:
	def read(self, filename):
		self.publications = []
		self.authors = []
		self.author_idx = {}

		handler = DocumentHandler(self)
		parser = make_parser()
		parser.setContentHandler(handler)
		infile = open(filename, "r")
		valid = True
		try:
			parser.parse(infile)
		except SAXException as e:
			valid = False
			print "Error reading file ("+e.getMessage()+")"
		infile.close()
		return valid

	def get_publication_summary(self):
		header = ( "Details", "Conference Paper", 
			"Journal", "Book", "Book Chapter", "Total" )

		plist = [0,0,0,0]
		alist = [set(),set(),set(),set()]

		for p in self.publications:
			plist[p.pub_type] += 1
			for a in p.authors:
				alist[p.pub_type].add(a)
		# create union of all authors
		ua = alist[0] | alist[1] | alist[2] | alist[3]

		data = [
			["Number of publications"] + plist + [sum(plist)],
			["Number of authors"] + [ len(a) for a in alist ] + [len(ua)] ]
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
			"Number of book chapers", "Total" )

		ystats = {}
		for p in self.publications:
			try:
				ystats[p.year][p.pub_type] += 1
			except KeyError:
				ystats[p.year] = [0,0,0,0]
				ystats[p.year][p.pub_type] += 1

		data = [ [y]+ystats[y]+[sum(ystats[y])] for y in ystats ]
		return (header, data)	

	def get_author_totals_by_year(self):
		header = ( "Year", "Number of conference papers",
			"Number of journals", "Number of books",
			"Number of book chapers", "Total" )

		ystats = {}
		for p in self.publications:
			try:
				s = ystats[p.year][p.pub_type]
			except KeyError:
				ystats[p.year] = [set(), set(), set(), set()]
				s = ystats[p.year][p.pub_type]
			for a in p.authors:
				s.add(a)
		data = [ [y]+[len(s) for s in ystats[y]]+[len(ystats[y][0] | ystats[y][1] | ystats[y][2] | ystats[y][3])]
			for y in ystats ]
		return (header, data)	

	def add_publication(self, pub_type, title, year, authors):
		if title == None or year == None or len(authors) == 0:
			print "Warning: excluding publication due to missing information"
			print "    Publication type:", PublicationType[pub_type]
			print "    Title:", title
			print "    Year:", year
			print "    Authors:", ",".join(authors)
			return
		idlist = []
		for a in authors:
			try:
				idlist.append(self.author_idx[a])
			except KeyError:
				a_id = len(self.authors)
				self.author_idx[a] = a_id
				idlist.append(a_id)
				self.authors.append(Author(a))
		self.publications.append(
			Publication(pub_type, title, year, idlist))
		if (len(self.publications) % 100000) == 0:
			print "Adding publication number %d (number of authors is %d)" % (len(self.publications), len(self.authors))

class DocumentHandler(handler.ContentHandler):
	PUB_TYPE = {
		"inproceedings":Publication.CONFERENCE_PAPER,
		"article":Publication.JOURNAL,
		"book":Publication.BOOK,
		"incollection":Publication.BOOK_CHAPTER }

	def __init__(self, db):
		self.tag = None
		self.chrs = ""
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
		self.chrs = ""
			
	def endElement(self, name):
		if self.pub_type == None:
			return
		d = self.chrs.strip()
		if self.tag == "author":
			self.authors.append(d)
		elif self.tag == "title":
			self.title = d
		elif self.tag == "year":
			self.year = d
		elif name in DocumentHandler.PUB_TYPE.keys():
			self.db.add_publication(
				self.pub_type,
				self.title,
				self.year,
				self.authors)
			self.clearData()
		self.tag = None
		self.chrs = ""

	def characters(self, chrs):
		if self.pub_type != None:
			self.chrs += chrs

