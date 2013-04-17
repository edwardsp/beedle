import sys
import database

if __name__ == "__main__":
	db = database.Database()
	db.read(sys.argv[1])
	h, d = db.get_crossfilter_data()
	print '"%s","%s","%s"' % h
	for x in d:
		print '%s,%s,%s' % (str(x[0]), str(x[1]), str(x[2]))

