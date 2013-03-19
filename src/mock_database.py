
class MockDatabase:
        def read(self, filename):
                pass

        def get_publication_summary(self):
                return [
	{ 'Number of publications' : { 'Conference Paper':10, 'Journal':5, 'Book':8, 'Book Chapter':2 } },
	{ 'Number of authors' : { 'Conference Paper':10, 'Journal':5, 'Book':8, 'Book Chapter':2 } }
]

        def get_publications_by_author(self):
                return [ ('Author1', 1, 2, 3, 4), ('Author2', 5, 6, 7, 8) ]

        def get_publications_by_year(self):
                return [ (2002, 100, 50, 25, 10), (2004, 99, 49, 24, 9) ]

        def get_author_totals_by_year(self):
                return [ (2001, 10, 5, 6, 3), (2003, 12, 7, 4, 2) ]

