
class MockDatabase:
        def read(self, filename):
                pass

        def get_publication_summary(self):
                return [
	{ 'Number of publications' : { 'Conference Paper':10, 'Journal':5, 'Book':8, 'Book Chapter':2 } },
	{ 'Number of authors' : { 'Conference Paper':10, 'Journal':5, 'Book':8, 'Book Chapter':2 } }
]

	# Return tuple containing headers and list of data
        def get_publications_by_author(self):
                return (('Author', 'Number of conference papers', 'Number of journals', 'Number of books', 'Number of book chapters', 'Total'), [ ('Author1', 1, 2, 3, 4, 10), ('Author2', 5, 6, 7, 8, 26) ])
	# Return tuple containing headers and list of data
        def get_publications_by_year(self):
                return (('Author', 'Number of conference papers', 'Number of journals', 'Number of books', 'Number of book chapters'), [ (2002, 100, 50, 25, 10), (2004, 99, 49, 24, 9) ])

	# Return tuple containing headers and list of data
        def get_author_totals_by_year(self):
                return (('Author', 'Number of conference papers', 'Number of journals', 'Number of books', 'Number of book chapters'), [ (2001, 10, 5, 6, 3), (2003, 12, 7, 4, 2) ])

